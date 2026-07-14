from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.finding import Finding
from app.models.risk_assessment import RiskAssessment
from app.services.risk_scoring import calculate_risk

router = APIRouter(
    prefix="/findings",
    tags=["Findings"]
)


@router.get("/demo")
def create_demo_finding(
    db: Session = Depends(get_db)
):

    try:
        # Create Finding
        finding = Finding(
            asset_id=101,
            hostname="web-prod-01",
            cve_id="CVE-2025-12345",
            title="Remote Code Execution",
            severity="Critical",
            cvss_score=9.8,
            epss_score=0.92,
            criticality="Critical",
            exposure_context="Internet-facing",
            exploit_available=True,
            status="OPEN"
        )

        print("Creating Finding...")

        # Save Finding
        db.add(finding)
        db.commit()
        db.refresh(finding)

        print(f"Finding Saved. ID = {finding.id}")

        # Calculate Risk
        result = calculate_risk(
            cvss_score=finding.cvss_score,
            epss_score=finding.epss_score,
            criticality=finding.criticality,
            exploit_available=finding.exploit_available,
            exposure_context=finding.exposure_context
        )

        print(result)

        # Save Risk Assessment
        risk = RiskAssessment(
            finding_id=finding.id,
            risk_score=result["risk_score"],
            priority=result["priority"]
        )

        db.add(risk)
        db.commit()
        db.refresh(risk)

        print(f"Risk Saved. ID = {risk.id}")

        return {
            "message": "Finding and Risk Assessment saved successfully",
            "finding_id": finding.id,
            "risk_score": risk.risk_score,
            "priority": risk.priority
        }

    except Exception as e:
        db.rollback()
        print("DATABASE ERROR:", str(e))
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
