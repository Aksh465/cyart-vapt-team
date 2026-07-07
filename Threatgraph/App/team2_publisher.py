import asyncio
import json
from nats.aio.client import Client as NATS


async def main():
    nc = NATS()

    await nc.connect("nats://localhost:4222")

    payload = {
        "asset_id": 101,
        "hostname": "web-prod-01",
        "cve_id": "CVE-2025-12345",
        "title": "Remote Code Execution",
        "severity": "Critical",
        "cvss_score": 9.8,
        "epss_score": 0.92,
        "criticality": "Critical",
        "exposure_context": "Internet-facing",
        "exploit_available": True,
        "status": "OPEN"
    }

    await nc.publish(
        "team2.findings",
        json.dumps(payload).encode()
    )

    print("Message Published Successfully")

    await nc.flush()
    await nc.close()


asyncio.run(main())