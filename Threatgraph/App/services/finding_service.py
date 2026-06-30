from sqlalchemy.orm import Session

from app.models.finding import Finding
from app.models.risk_assessment import RiskAssessment

from app.services.risk_scoring import calculate_risk
from app.services.nats_publisher import publish_risk


async def process_finding(data: dict, db: Session):

    finding = Finding(**data)

    db.add(finding)
    db.commit()
    db.refresh(finding)

    result = calculate_risk(
        cvss_score=finding.cvss_score,
        epss_score=finding.epss_score,
        criticality=finding.criticality,
        exploit_available=finding.exploit_available,
        exposure_context=finding.exposure_context
    )

    risk = RiskAssessment(
        finding_id=finding.id,
        risk_score=result["risk_score"],
        priority=result["priority"]
    )

    db.add(risk)
    db.commit()
    db.refresh(risk)

    payload = {
        "finding_id": finding.id,
        "asset_id": finding.asset_id,
        "hostname": finding.hostname,
        "cve_id": finding.cve_id,
        "risk_score": risk.risk_score,
        "priority": risk.priority,
        "status": finding.status
    }

    await publish_risk(payload)

    return payload