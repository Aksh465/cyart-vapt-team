from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class FindingBase(BaseModel):
    asset_id: int
    hostname: str

    cve_id: str

    title: str

    severity: str

    cvss_score: float

    epss_score: float = 0.0

    criticality: str

    exploit_available: bool = False

    status: str = "OPEN"


class FindingCreate(FindingBase):
    pass


class FindingResponse(FindingBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )