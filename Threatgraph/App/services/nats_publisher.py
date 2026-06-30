import json

from nats.aio.client import Client as NATS

from app.core.config import settings


async def publish_risk(payload: dict):
    """
    Publish risk assessment to Team 4
    """

    nc = NATS()

    await nc.connect(settings.NATS_URL)

    await nc.publish(
        "team3.risk.assessed",
        json.dumps(payload).encode()
    )

    await nc.flush()

    print(f"Published Risk: {payload['cve_id']}")

    await nc.close()