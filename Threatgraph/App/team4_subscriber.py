import asyncio
import json

from nats.aio.client import Client as NATS


async def message_handler(msg):
    """
    Receives Risk Assessment from Team 3
    """

    data = json.loads(msg.data.decode())

    print("\n==========================================")
    print("      TEAM 4 - RISK ASSESSMENT RECEIVED")
    print("==========================================")

    print(f"Finding ID : {data['finding_id']}")
    print(f"Asset ID   : {data['asset_id']}")
    print(f"Hostname   : {data['hostname']}")
    print(f"CVE ID     : {data['cve_id']}")
    print(f"Risk Score : {data['risk_score']}")
    print(f"Priority   : {data['priority']}")
    print(f"Status     : {data['status']}")

    print("------------------------------------------")
    print("Team 4 Processing Started...")

    # ===========================================
    # Team 4 Logic Starts Here
    # ===========================================

    # Save to Database
    # save_to_database(data)

    # Generate Alert
    # generate_alert(data)

    # Create Ticket
    # create_ticket(data)

    # Send Email
    # send_email(data)

    print("Processing Completed")
    print("==========================================\n")


async def main():
    nc = NATS()

    try:
        print("Connecting to NATS...")

        await nc.connect("nats://localhost:4222")

        print("Connected Successfully")

        await nc.subscribe(
            "team3.risk.assessed",
            cb=message_handler
        )

        print("\nWaiting for Risk Assessments from Team 3...")
        print("Listening on subject: team3.risk.assessed\n")

        while True:
            await asyncio.sleep(1)

    except Exception as e:
        print(f"\nConnection Error: {e}")

    finally:
        if nc.is_connected:
            await nc.close()


if __name__ == "__main__":
    asyncio.run(main())