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
                "cve_id": "CVE-2021-44228",
                "title": "Apache Log4j Remote Code Execution",
                "severity": "Critical",
                "cvss_score": 10.0,
                "epss_score": 0.99,
                "criticality": "Critical",
                "exposure_context": "Internet-facing",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 102,
                "hostname": "vpn-gateway-01",
                "cve_id": "CVE-2024-3400",
                "title": "Palo Alto PAN-OS Command Injection",
                "severity": "Critical",
                "cvss_score": 10.0,
                "epss_score": 0.98,
                "criticality": "Critical",
                "exposure_context": "Internet-facing",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 103,
                "hostname": "jenkins-master",
                "cve_id": "CVE-2024-23897",
                "title": "Jenkins CLI Arbitrary File Read",
                "severity": "Critical",
                "cvss_score": 9.8,
                "epss_score": 0.95,
                "criticality": "High",
                "exposure_context": "Internet-facing",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 104,
                "hostname": "mail-server",
                "cve_id": "CVE-2021-26855",
                "title": "Microsoft Exchange ProxyLogon",
                "severity": "Critical",
                "cvss_score": 9.8,
                "epss_score": 0.97,
                "criticality": "Critical",
                "exposure_context": "Internet-facing",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 105,
                "hostname": "file-server",
                "cve_id": "CVE-2017-0144",
                "title": "SMB EternalBlue",
                "severity": "Critical",
                "cvss_score": 8.8,
                "epss_score": 0.96,
                "criticality": "High",
                "exposure_context": "Internal",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 106,
                "hostname": "backup-server",
                "cve_id": "CVE-2023-4966",
                "title": "Citrix Bleed",
                "severity": "Critical",
                "cvss_score": 9.4,
                "epss_score": 0.97,
                "criticality": "Critical",
                "exposure_context": "Internet-facing",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 107,
                "hostname": "finance-db",
                "cve_id": "CVE-2023-3519",
                "title": "Citrix ADC Remote Code Execution",
                "severity": "Critical",
                "cvss_score": 9.8,
                "epss_score": 0.94,
                "criticality": "Critical",
                "exposure_context": "Internet-facing",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 108,
                "hostname": "vpn-appliance",
                "cve_id": "CVE-2019-19781",
                "title": "Citrix ADC Path Traversal",
                "severity": "Critical",
                "cvss_score": 9.8,
                "epss_score": 0.92,
                "criticality": "High",
                "exposure_context": "Internet-facing",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 109,
                "hostname": "dev-web-01",
                "cve_id": "CVE-2023-34362",
                "title": "MOVEit Transfer SQL Injection",
                "severity": "Critical",
                "cvss_score": 9.8,
                "epss_score": 0.91,
                "criticality": "High",
                "exposure_context": "Internet-facing",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 110,
                "hostname": "hr-portal",
                "cve_id": "CVE-2022-1388",
                "title": "F5 BIG-IP Authentication Bypass",
                "severity": "Critical",
                "cvss_score": 9.8,
                "epss_score": 0.89,
                "criticality": "Critical",
                "exposure_context": "Internet-facing",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 111,
                "hostname": "linux-app-01",
                "cve_id": "CVE-2022-0847",
                "title": "Dirty Pipe",
                "severity": "High",
                "cvss_score": 7.8,
                "epss_score": 0.63,
                "criticality": "High",
                "exposure_context": "Internal",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 112,
                "hostname": "git-server",
                "cve_id": "CVE-2022-24765",
                "title": "Git Directory Traversal",
                "severity": "High",
                "cvss_score": 7.8,
                "epss_score": 0.41,
                "criticality": "Medium",
                "exposure_context": "Internal",
                "exploit_available": False,
                "status": "OPEN"
            },
            {
                "asset_id": 113,
                "hostname": "oracle-db",
                "cve_id": "CVE-2020-14882",
                "title": "Oracle WebLogic RCE",
                "severity": "Critical",
                "cvss_score": 9.8,
                "epss_score": 0.85,
                "criticality": "High",
                "exposure_context": "Restricted",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 114,
                "hostname": "docker-host",
                "cve_id": "CVE-2019-5736",
                "title": "runC Container Escape",
                "severity": "High",
                "cvss_score": 8.6,
                "epss_score": 0.48,
                "criticality": "High",
                "exposure_context": "Internal",
                "exploit_available": False,
                "status": "OPEN"
            },
            {
                "asset_id": 115,
                "hostname": "k8s-master",
                "cve_id": "CVE-2018-1002105",
                "title": "Kubernetes API Privilege Escalation",
                "severity": "High",
                "cvss_score": 8.8,
                "epss_score": 0.52,
                "criticality": "Critical",
                "exposure_context": "Internal",
                "exploit_available": False,
                "status": "OPEN"
            },
            {
                "asset_id": 116,
                "hostname": "monitoring-server",
                "cve_id": "CVE-2021-3156",
                "title": "Baron Samedit Sudo Privilege Escalation",
                "severity": "High",
                "cvss_score": 7.8,
                "epss_score": 0.58,
                "criticality": "Medium",
                "exposure_context": "Restricted",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 117,
                "hostname": "dev-linux",
                "cve_id": "CVE-2021-4034",
                "title": "Polkit pkexec Privilege Escalation",
                "severity": "High",
                "cvss_score": 7.8,
                "epss_score": 0.61,
                "criticality": "Medium",
                "exposure_context": "Internal",
                "exploit_available": True,
                "status": "OPEN"
            },
            {
                "asset_id": 118,
                "hostname": "test-app",
                "cve_id": "CVE-2020-0796",
                "title": "SMBGhost",
                "severity": "High",
                "cvss_score": 8.1,
                "epss_score": 0.54,
                "criticality": "Medium",
                "exposure_context": "Restricted",
                "exploit_available": False,
                "status": "OPEN"
            },
            {
                "asset_id": 119,
                "hostname": "internal-api",
                "cve_id": "CVE-2023-44487",
                "title": "HTTP/2 Rapid Reset",
                "severity": "High",
                "cvss_score": 7.5,
                "epss_score": 0.39,
                "criticality": "Medium",
                "exposure_context": "Internet-facing",
                "exploit_available": False,
                "status": "OPEN"
            },
            {
                "asset_id": 120,
                "hostname": "legacy-app",
                "cve_id": "CVE-2021-41773",
                "title": "Apache HTTP Server Path Traversal",
                "severity": "High",
                "cvss_score": 7.5,
                "epss_score": 0.72,
                "criticality": "Low",
                "exposure_context": "Internal",
                "exploit_available": True,
                "status": "OPEN"
            }
        ]

    for payload in findings:

        await nc.publish(
            "team2.findings",
            json.dumps(payload).encode()
        )

        print(f"Published: {payload['cve_id']}")

        await asyncio.sleep(0.5)

    await nc.flush()

    await nc.close()

    print("\nAll 20 findings published successfully.")


if __name__ == "__main__":
    asyncio.run(main())