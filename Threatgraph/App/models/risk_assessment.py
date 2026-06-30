from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from app.core.database import Base


class RiskAssessment(Base):
    __tablename__ = "risk_assessments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    finding_id = Column(
        Integer,
        nullable=False
    )

    risk_score = Column(
        Float,
        nullable=False
    )

    priority = Column(
        String(50),
        nullable=False
    )

    recommendation = Column(
        String(500),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )