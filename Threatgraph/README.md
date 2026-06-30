# ThreatGraph – Team 3 Risk Assessment Service

## Overview

ThreatGraph Team 3 is responsible for calculating vulnerability risk scores received from Team 2, storing findings and risk assessments in PostgreSQL, and publishing the assessed risk to Team 4 using NATS messaging.

The service provides both:

- REST APIs (FastAPI) for testing and manual execution.
- NATS Subscriber for real-time processing from Team 2.

---

# Architecture

```
                  Team 2
                     │
                     │ (Finding)
                     ▼
             NATS Subscriber
                     │
                     ▼
            Finding Service
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 Store Finding   Calculate Risk   Store Risk
      │
      ▼
      Publish Risk
      │
      ▼
                 Team 4
```

---

# Features

- FastAPI REST APIs
- PostgreSQL Integration
- SQLAlchemy ORM
- Risk Score Calculation
- NATS Subscriber
- NATS Publisher
- Pydantic Models
- Environment Configuration using `.env`

---

# Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic v2
- NATS Messaging

---

# Project Structure

```
app/
│
├── api/
│   ├── findings.py
│   └── risks.py
│
├── core/
│   ├── config.py
│   └── database.py
│
├── models/
│   ├── finding.py
│   └── risk_assessment.py
│
├── schemas/
│   ├── finding.py
│   └── risk.py
│
├── services/
│   ├── finding_service.py
│   ├── risk_scoring.py
│   ├── nats_publisher.py
│   └── nats_subscriber.py
│
├── create_tables.py
└── main.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/ThreatGraph-Team3.git

cd ThreatGraph-Team3
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
APP_NAME=ThreatGraph

SECRET_KEY=mysecretkey

ALGORITHM=HS256

DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/postgres

NATS_URL=nats://localhost:4222

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# Create Database Tables

Run

```bash
python -m app.create_tables
```

Expected output

```
Tables created successfully
```

---

# Running the Application

```bash
uvicorn app.main:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Home

```
GET /
```

Response

```json
{
  "message": "ThreatGraph Running"
}
```

---

## Create Demo Finding

```
GET /findings/demo
```

Creates:

- Finding
- Risk Assessment

Stores both into PostgreSQL.

---

## Calculate Risk

```
POST /risk/calculate/{finding_id}
```

Example

```
POST /risk/calculate/1
```

Creates a new Risk Assessment for an existing finding.

---

# NATS Subjects

## Receive Findings (Team 2 → Team 3)

```
team2.findings
```

Subscriber automatically:

- Receives Finding
- Stores Finding
- Calculates Risk
- Stores Risk Assessment
- Publishes Result

---

## Publish Risk (Team 3 → Team 4)

```
team3.risk.assessed
```

Published payload

```json
{
    "finding_id":1,
    "asset_id":101,
    "hostname":"web-prod-01",
    "cve_id":"CVE-2025-12345",
    "risk_score":9.61,
    "priority":"CRITICAL",
    "status":"OPEN"
}
```

---

# Risk Scoring Formula

Composite Risk Score is calculated using:

- CVSS Score
- EPSS Score
- Asset Criticality
- Exposure Context
- Exploit Availability (KEV)

Priority Mapping

| Score | Priority |
|--------|----------|
| >= 8 | CRITICAL |
| >= 5 | HIGH |
| >= 3 | MEDIUM |
| < 3 | LOW |

---

# Workflow

```
Team 2
   │
   ▼
Publish Finding
(team2.findings)
   │
   ▼
NATS Subscriber
   │
   ▼
Finding Service
   │
   ├── Store Finding
   ├── Calculate Risk
   ├── Store Risk Assessment
   └── Publish Risk
             │
             ▼
          Team 4
```

---

# Database Tables

## findings

Stores incoming vulnerability findings.

Fields include

- Asset ID
- Hostname
- CVE ID
- Severity
- CVSS
- EPSS
- Criticality
- Exposure Context
- Status

---

## risk_assessments

Stores calculated risk information.

Fields include

- Finding ID
- Risk Score
- Priority
- Recommendation
- Created At

---

# Requirements

- Python 3.13+
- PostgreSQL
- NATS Server

---

# Author

**Akash Bangera**

B.Sc. Information Technology

ThreatGraph Team 3 – Risk Assessment Service
