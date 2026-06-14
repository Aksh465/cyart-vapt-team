import json
from pydantic import BaseModel, computed_field


class Finding(BaseModel):
    asset_id: int
    hostname: str
    cve_id: str
    title: str
    severity: str
    cvss_score: float  # e.g., 9.8
    epss_score: float  # e.g., 0.92
    criticality: str  # Low, Medium, High, Critical
    exposure_context: str  # Restricted, Internal, Internet-facing
    exploit_available: bool  # Maps to KEV status
    status: str

    @computed_field
    @property
    def composite_risk_score(self) -> float:
        # 1. Base Score = CVSS_Base × 10
        base_score = self.cvss_score * 10

        # 2. Exploit Likelihood = EPSS × 100
        exploit_likelihood = self.epss_score * 100

        # 3. KEV Multiplier = 1.5 if KEV-listed, else 1.0
        kev_multiplier = 1.5 if self.exploit_available else 1.0

        # 4. Asset Weight Mapping
        asset_weights = {
            "low": 1.0,
            "medium": 1.5,
            "high": 2.0,
            "critical": 3.0
        }
        asset_weight = asset_weights.get(self.criticality.lower(), 1.0)

        # 5. Exposure Multiplier Mapping
        exposure_multipliers = {
            "restricted": 1.0,
            "internal": 1.5,
            "internet-facing": 2.5
        }
        exposure_multiplier = exposure_multipliers.get(self.exposure_context.lower(), 1.0)

        # 6. Normalization Factor
        # Max theoretical raw score = (100 * 100 * 1.5 * 3.0 * 2.5) = 112,500
        # Dividing by 1125.0 brings the absolute maximum score to exactly 100.0
        normalization_factor = 1125.0

        # Calculate raw score
        raw_score = (
                base_score *
                exploit_likelihood *
                kev_multiplier *
                asset_weight *
                exposure_multiplier
        )

        # Normalize and round to 2 decimal places
        final_score = raw_score / normalization_factor
        return round(final_score, 2)


# --- Simulated API Response Payload ---
mock_api_payload = """
[
    {
        "asset_id": 101,
        "hostname": "web-prod-01",
        "cve_id": "CVE-2025-12345",
        "title": "Remote Code Execution",
        "severity": "Critical",
        "cvss_score": 9.8,
        "epss_score": 0.92,
        "criticality": "Critical",
        "exposure_context": "Internet-facing",
        "exploit_available": true,
        "status": "OPEN"
    },
    {
        "asset_id": 102,
        "hostname": "internal-tool-02",
        "cve_id": "CVE-2026-9999",
        "title": "SQL Injection",
        "severity": "High",
        "cvss_score": 8.5,
        "epss_score": 0.12,
        "criticality": "Medium",
        "exposure_context": "Internal",
        "exploit_available": false,
        "status": "OPEN"
    }
]
"""

# Parse and process
raw_data = json.loads(mock_api_payload)
findings = [Finding(**item) for item in raw_data]

# Print Output
for f in findings:
    print(f"Host: {f.hostname} | CVE: {f.cve_id} | New Composite Score: {f.composite_risk_score}/100.0")
