from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class Finding(Base):

    __tablename__ = "findings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    asset_id = Column(
        Integer,
        ForeignKey("assets.id"),
        nullable=False
    )

    scanner = Column(
        String(50),
        nullable=False
    )

    title = Column(
        String(500),
        nullable=False
    )

    description = Column(
        String(2000),
        nullable=True
    )

    cve_id = Column(
        String(100),
        nullable=True
    )

    severity = Column(
        String(50),
        nullable=False
    )

    cvss_score = Column(
        Float,
        default=0.0
    )

    epss_score = Column(
        Float,
        default=0.0
    )

    kev_listed = Column(
        Boolean,
        default=False
    )

    risk_score = Column(
        Float,
        default=0.0
    )

    priority = Column(
        String(20),
        default="P4"
    )

    status = Column(
        String(50),
        default="Open"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )