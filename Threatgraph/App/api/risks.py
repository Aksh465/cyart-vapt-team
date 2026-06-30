from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.finding import Finding
from app.models.risk_assessment import RiskAssessment
from app.services.risk_scoring import calculate_risk

router = APIRouter(
    prefix="/risk",
    tags=["Risk Assessment"]
)


@router.post("/calculate/{finding_id}")
def calculate_finding_risk(
    finding_id: int,
    db: Session = Depends(get_db)
):

    # Get Finding
    finding = db.query(Finding).filter(
        Finding.id == finding_id
    ).first()

    if not finding:
        raise HTTPException(
            status_code=404,
            detail="Finding not found"
        )

    # Calculate Risk
    result = calculate_risk(
        cvss_score=finding.cvss_score,
        epss_score=finding.epss_score,
        criticality=finding.criticality,
        exploit_available=finding.exploit_available,
        exposure_context=finding.exposure_context
    )

    # ALWAYS Create New Risk Assessment
    risk = RiskAssessment(
        finding_id=finding.id,
        risk_score=result["risk_score"],
        priority=result["priority"]
    )

    db.add(risk)
    db.commit()
    db.refresh(risk)

    return {
        "message": "Risk Assessment Created Successfully",
        "risk_assessment_id": risk.id,
        "finding_id": finding.id,
        "risk_score": risk.risk_score,
        "priority": risk.priority
    }