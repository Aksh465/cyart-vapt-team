import asyncio
import json

from nats.aio.client import Client as NATS

from app.core.config import settings
from app.core.database import SessionLocal
from app.services.finding_service import process_finding


async def message_handler(msg):

    data = json.loads(msg.data.decode())

    print("\nReceived Finding")
    print(data)

    db = SessionLocal()

    try:
        await process_finding(data, db)

    except Exception as e:
        db.rollback()
        print("ERROR:", e)

    finally:
        db.close()


async def start_subscriber():

    nc = NATS()

    await nc.connect(settings.NATS_URL)

    await nc.subscribe(
        "team2.findings",
        cb=message_handler
    )

    print("Listening on subject: team2.findings")

    while True:
        await asyncio.sleep(1)