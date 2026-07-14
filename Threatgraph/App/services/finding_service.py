from sqlalchemy.orm import Session

from app.models.finding import Finding
from app.models.risk_assessment import RiskAssessment
from app.models.vulnerability_cache import VulnerabilityCache

from app.services.vulnerability_enrichment import enrich_vulnerability
from app.services.risk_scoring import calculate_risk
from app.services.nats_publisher import publish_risk


async def process_finding(data: dict, db: Session):

    title = data["title"].strip()

    print("\n====================================")
    print("TEAM 3 PROCESSING")
    print("====================================")
    print(f"Finding Title : {title}")

    # =====================================================
    # STEP 1 : Check Vulnerability Cache
    # =====================================================

    cache = db.query(
        VulnerabilityCache
    ).filter(
        VulnerabilityCache.title.ilike(title)
    ).first()

    if cache:

        print("Source : Vulnerability Cache")

        vuln = {

            "cve_id": cache.cve_id,

            "title": cache.title,

            "cvss_score": cache.cvss_score,

            "epss_score": cache.epss_score,

            "criticality": cache.criticality

        }

    else:

        print("Source : Internet / Knowledge Base")

        vuln = enrich_vulnerability(title)

        cache = VulnerabilityCache(

            title=title,

            cve_id=vuln["cve_id"],

            severity=data["severity"],

            cvss_score=vuln["cvss_score"],

            epss_score=vuln["epss_score"],

            criticality=vuln["criticality"],

            exploit_available=data["exploit_available"]

        )

        db.add(cache)
        db.commit()
        db.refresh(cache)

        print("Saved into Vulnerability Cache")

    # =====================================================
    # STEP 2 : Save Finding
    # =====================================================

    finding = Finding(

        asset_id=data["asset_id"],

        hostname=data["hostname"],

        title=title,

        cve_id=vuln["cve_id"],

        severity=data["severity"],

        cvss_score=vuln["cvss_score"],

        epss_score=vuln["epss_score"],

        criticality=vuln["criticality"],

        exposure_context=data["exposure_context"],

        exploit_available=data["exploit_available"],

        status=data["status"]

    )

    db.add(finding)
    db.commit()
    db.refresh(finding)

    print(f"Finding Stored (ID={finding.id})")

    # =====================================================
    # STEP 3 : Calculate Risk
    # =====================================================

    risk_result = calculate_risk(

        cvss_score=finding.cvss_score,

        epss_score=finding.epss_score,

        criticality=finding.criticality,

        exploit_available=finding.exploit_available,

        exposure_context=finding.exposure_context

    )

    print(f"Risk Score : {risk_result['risk_score']}")
    print(f"Priority   : {risk_result['priority']}")

    # =====================================================
    # STEP 4 : Save Risk Assessment
    # =====================================================

    risk = RiskAssessment(

        finding_id=finding.id,

        risk_score=risk_result["risk_score"],

        priority=risk_result["priority"]

    )

    db.add(risk)
    db.commit()
    db.refresh(risk)

    print(f"Risk Assessment Stored (ID={risk.id})")

    # =====================================================
    # STEP 5 : Publish to Team 4
    # =====================================================

    payload = {

        "finding_id": finding.id,

        "asset_id": finding.asset_id,

        "hostname": finding.hostname,

        "title": finding.title,

        "cve_id": finding.cve_id,

        "severity": finding.severity,

        "cvss_score": finding.cvss_score,

        "epss_score": finding.epss_score,

        "criticality": finding.criticality,

        "exposure_context": finding.exposure_context,

        "exploit_available": finding.exploit_available,

        "risk_score": risk.risk_score,

        "priority": risk.priority,

        "status": finding.status

    }

    await publish_risk(payload)

    print("\nPublished Risk Assessment to Team 4")
    print("====================================\n")

    return payload
