from datetime import datetime

from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Boolean
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class Asset(Base):

    __tablename__ = "assets"

    # -------------------------
    # Primary Key
    # -------------------------

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    # -------------------------
    # Asset Details
    # -------------------------

    hostname: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    ip_address: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    domain: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    operating_system: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    asset_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Examples:
    # server
    # workstation
    # container
    # kubernetes
    # database

    # -------------------------
    # Criticality
    # -------------------------

    criticality: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="LOW"
    )

    # LOW
    # MEDIUM
    # HIGH
    # CRITICAL

    exposure: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="INTERNAL"
    )

    # INTERNAL
    # INTERNET
    # RESTRICTED

    environment: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="PRODUCTION"
    )

    # DEV
    # TEST
    # STAGING
    # PRODUCTION

    # -------------------------
    # Ownership
    # -------------------------

    owner: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    business_unit: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    # -------------------------
    # Metadata
    # -------------------------

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    # -------------------------
    # Audit
    # -------------------------

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # -------------------------
    # Relationships
    # -------------------------

    vulnerabilities = relationship(
        "Vulnerability",
        back_populates="asset",
        cascade="all, delete-orphan"
    )

    risks = relationship(
        "RiskScore",
        back_populates="asset",
        cascade="all, delete-orphan"
    )

    attack_paths = relationship(
        "AttackPath",
        back_populates="asset",
        cascade="all, delete-orphan"
    )