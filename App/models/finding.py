from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime

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
        nullable=False
    )

    hostname = Column(
        String(255),
        nullable=False
    )

    cve_id = Column(
        String(100),
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    severity = Column(
        String(50),
        nullable=False
    )

    cvss_score = Column(
        Float,
        nullable=False
    )

    epss_score = Column(
        Float,
        default=0.0
    )

    criticality = Column(
        String(50),
        nullable=False
    )

    exploit_available = Column(
        Boolean,
        default=False
    )

    status = Column(
        String(50),
        default="OPEN"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )