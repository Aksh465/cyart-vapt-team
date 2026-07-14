from app.core.database import Base
from app.core.database import engine

from app.models.finding import Finding
from app.models.risk_assessment import RiskAssessment
from app.models.vulnerability_cache import VulnerabilityCache


def create_tables():

    Base.metadata.create_all(
        bind=engine
    )

    print("Tables created successfully")


if __name__=="__main__":

    create_tables()
