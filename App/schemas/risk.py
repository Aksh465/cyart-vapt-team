from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RiskBase(BaseModel):
    finding_id: int

    risk_score: float

    priority: str

    recommendation: Optional[str] = None


class RiskCreate(RiskBase):
    pass


from pydantic import BaseModel, ConfigDict

class RiskResponse(RiskBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )