import asyncio
import json

from nats.aio.client import Client as NATS


async def main():

    nc = NATS()

    await nc.connect("nats://localhost:4222")

    findings = [

        {
            "asset_id": 101,
            "hostname": "web-prod-01",
            "title": "Apache Log4j Remote Code Execution",
            "severity": "Critical",
            "exposure_context": "Internet-facing",
            "exploit_available": True,
            "status": "OPEN"
        },

        {
            "asset_id": 102,
            "hostname": "vpn-gateway-01",
            "title": "Palo Alto PAN-OS Command Injection",
            "severity": "Critical",
            "exposure_context": "Internet-facing",
            "exploit_available": True,
            "status": "OPEN"
        },

        {
            "asset_id": 103,
            "hostname": "exchange-server",
            "title": "Microsoft Exchange ProxyLogon",
            "severity": "Critical",
            "exposure_context": "Internet-facing",
            "exploit_available": True,
            "status": "OPEN"
        },

        {
            "asset_id": 104,
            "hostname": "file-server",
            "title": "SMB EternalBlue",
            "severity": "High",
            "exposure_context": "Internal",
            "exploit_available": True,
            "status": "OPEN"
        },

        {
            "asset_id": 105,
            "hostname": "jenkins-master",
            "title": "Jenkins CLI Arbitrary File Read",
            "severity": "High",
            "exposure_context": "Internet-facing",
            "exploit_available": True,
            "status": "OPEN"
        },

        {
            "asset_id": 106,
            "hostname": "spring-api",
            "title": "Spring4Shell",
            "severity": "Critical",
            "exposure_context": "Internet-facing",
            "exploit_available": True,
            "status": "OPEN"
        },

        {
            "asset_id": 107,
            "hostname": "struts-server",
            "title": "Apache Struts RCE",
            "severity": "Critical",
            "exposure_context": "Internet-facing",
            "exploit_available": True,
            "status": "OPEN"
        },

        {
            "asset_id": 108,
            "hostname": "gitlab-prod",
            "title": "GitLab Account Takeover",
            "severity": "High",
            "exposure_context": "Internet-facing",
            "exploit_available": False,
            "status": "OPEN"
        },

        {
            "asset_id": 109,
            "hostname": "fortigate-fw",
            "title": "Fortinet FortiOS Authentication Bypass",
            "severity": "Critical",
            "exposure_context": "Internet-facing",
            "exploit_available": True,
            "status": "OPEN"
        },

        {
            "asset_id": 110,
            "hostname": "moveit-server",
            "title": "MOVEit Transfer SQL Injection",
            "severity": "Critical",
            "exposure_context": "Internet-facing",
            "exploit_available": True,
            "status": "OPEN"
        }

    ]

    for finding in findings:

        await nc.publish(
            "team2.findings",
            json.dumps(finding).encode()
        )

        print(f"Published: {finding['title']}")

        await asyncio.sleep(1)

    await nc.flush()
    await nc.close()

    print("\nAll findings published successfully.")


if __name__ == "__main__":
    asyncio.run(main())
