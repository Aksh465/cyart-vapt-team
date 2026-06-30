import json
import asyncio

from pydantic import BaseModel, computed_field
from nats.aio.client import Client as NATS


class Finding(BaseModel):
    asset_id: int
    hostname: str
    cve_id: str
    title: str
    severity: str
    cvss_score: float
    epss_score: float
    criticality: str
    exposure_context: str
    exploit_available: bool
    status: str

    @computed_field
    @property
    def composite_risk_score(self) -> float:
        # 1. Base Score = CVSS_Base × 10
        base_score = self.cvss_score * 10

        # 2. Exploit Likelihood = EPSS × 100
        exploit_likelihood = self.epss_score * 100

        # 3. KEV Multiplier = 1.5 if KEV-listed, else 1.0
        kev_multiplier = 1.5 if self.exploit_available else 1.0

        # 4. Asset Weight Mapping
        asset_weights = {
            "low": 1.0,
            "medium": 1.5,
            "high": 2.0,
            "critical": 3.0
        }
        asset_weight = asset_weights.get(self.criticality.lower(), 1.0)

        # 5. Exposure Multiplier Mapping
        exposure_multipliers = {
            "restricted": 1.0,
            "internal": 1.5,
            "internet-facing": 2.5
        }
        exposure_multiplier = exposure_multipliers.get(
            self.exposure_context.lower(),
            1.0
        )

        # 6. Normalization Factor
        normalization_factor = 1125.0

        raw_score = (
            base_score *
            exploit_likelihood *
            kev_multiplier *
            asset_weight *
            exposure_multiplier
        )

        final_score = raw_score / normalization_factor
        return round(final_score, 2)


# =====================================
# ADD THIS FUNCTION
# Used by FastAPI endpoint
# =====================================

def calculate_risk(
    cvss_score: float,
    epss_score: float,
    criticality: str,
    exploit_available: bool,
    exposure_context: str = "Internet-facing"
):
    """
    Uses EXACT SAME FORMULA already defined above.
    """

    finding = Finding(
        asset_id=0,
        hostname="temp",
        cve_id="temp",
        title="temp",
        severity="temp",
        cvss_score=cvss_score,
        epss_score=epss_score,
        criticality=criticality,
        exposure_context=exposure_context,
        exploit_available=exploit_available,
        status="OPEN"
    )

    score = finding.composite_risk_score

    if score >= 8:
        priority = "CRITICAL"
    elif score >= 5:
        priority = "HIGH"
    elif score >= 3:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    return {
        "risk_score": score,
        "priority": priority
    }

