# ThreatGraph – Team 3 Risk Assessment Service

## Overview

ThreatGraph Team 3 is responsible for receiving vulnerability findings from Team 2, calculating composite risk scores, storing findings and risk assessments in PostgreSQL, and publishing the assessed risk to Team 4 using NATS messaging.

The service supports:

- Automatic real-time processing using **NATS Messaging**
- REST APIs (FastAPI) for development and manual testing

---

# Architecture

```
                     Team 2
             (team2_publisher.py)
                     │
                     │ Publish Finding
                     ▼
             NATS Subject
            team2.findings
                     │
                     ▼
          NATS Subscriber (Team 3)
     (app/services/nats_subscriber.py)
                     │
                     ▼
            Finding Service
     (app/services/finding_service.py)
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 Store Finding   Calculate Risk   Store Risk
      │
      ▼
 Publish Risk Assessment
      │
      ▼
     NATS Subject
team3.risk.assessed
      │
      ▼
Team 4 (team4_subscriber.py)
```

---

# Features

- FastAPI REST APIs
- PostgreSQL Integration
- SQLAlchemy ORM
- Composite Risk Score Calculation
- NATS Subscriber
- NATS Publisher
- Pydantic Models
- Environment Configuration using `.env`

---

# Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic v2
- NATS Messaging
- Uvicorn

---

# Project Structure

```
app/
│
├── api/
│   ├── findings.py          # Development API
│   └── risks.py             # Development API
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
│
├── team2_publisher.py
├── team4_subscriber.py
│
├── requirements.txt
├── .env
└── README.md
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

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
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

```bash
python -m app.create_tables
```

Expected Output

```
Tables created successfully
```

---

# Start NATS Server

```bash
nats-server
```

---

# Run Team 3

```bash
uvicorn app.main:app --reload
```

Expected Output

```
NATS Subscriber Started

Listening on subject:

team2.findings
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

# Simulate Team 2

Run

```bash
python team2_publisher.py
```

This publishes a sample vulnerability finding to

```
team2.findings
```

---

# Simulate Team 4 (Optional)

Open another terminal.

Run

```bash
python team4_subscriber.py
```

Expected Output

```
Waiting for Team 3 Risk Assessments...
```

Whenever Team 3 publishes a risk assessment, Team 4 receives

```
Finding ID

Asset ID

Hostname

CVE ID

Risk Score

Priority

Status
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

# Development APIs

The following APIs exist only for manual testing and development.

## Create Demo Finding

```
GET /findings/demo
```

Creates

- Finding
- Risk Assessment

Stores both in PostgreSQL.

**Not used in the production workflow.**

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

**Development/testing only.**

---

# NATS Subjects

## Receive Findings

```
team2.findings
```

The subscriber automatically

- Receives Finding
- Stores Finding
- Calculates Composite Risk
- Stores Risk Assessment
- Publishes Result

---

## Publish Risk

```
team3.risk.assessed
```

Published Payload

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

# Service Layer

## finding_service.py

Contains the core business logic.

Responsibilities

- Store Finding
- Calculate Composite Risk
- Store Risk Assessment
- Publish Risk Assessment

Separating business logic from the subscriber improves maintainability and allows reuse by APIs or future services.

---

## risk_scoring.py

Calculates the Composite Risk Score using

- CVSS Score
- EPSS Score
- Asset Criticality
- Exposure Context
- Exploit Availability (KEV)

Returns

- Risk Score
- Priority

---

## nats_subscriber.py

Subscribes to

```
team2.findings
```

Automatically processes incoming findings using the business logic.

---

## nats_publisher.py

Publishes processed risk assessments to

```
team3.risk.assessed
```

for Team 4.

---

# Risk Scoring Formula

Composite Risk Score is calculated using

- CVSS Score
- EPSS Score
- Asset Criticality
- Exposure Context
- Exploit Availability (KEV)

---

# Priority Mapping

| Score | Priority |
|--------|----------|
| ≥ 8 | CRITICAL |
| ≥ 5 | HIGH |
| ≥ 3 | MEDIUM |
| < 3 | LOW |

---

# Workflow

```
               TEAM 2

       team2_publisher.py
               │
               ▼
      Publish Finding
               │
               ▼
      team2.findings
               │
               ▼
      NATS Subscriber
               │
               ▼
      finding_service.py
               │
               ├── Store Finding
               ├── Calculate Risk
               ├── Store Risk
               └── Publish Risk
                        │
                        ▼
      team3.risk.assessed
                        │
                        ▼
      team4_subscriber.py
```

---

# Database Tables

## findings

Stores incoming vulnerability findings.

Fields

- Asset ID
- Hostname
- CVE ID
- Severity
- CVSS Score
- EPSS Score
- Criticality
- Exposure Context
- Status

---

## risk_assessments

Stores calculated risk information.

Fields

- Finding ID
- Risk Score
- Priority
- Recommendation
- Created At

---

# Testing Order

1. Start PostgreSQL

2. Start NATS

```bash
nats-server
```

3. Start Team 3

```bash
uvicorn app.main:app --reload
```

4. (Optional) Start Team 4

```bash
python team4_subscriber.py
```

5. Publish Sample Finding

```bash
python team2_publisher.py
```

Observe

- Finding stored
- Risk calculated
- Risk stored
- Risk published
- Team 4 receives processed message

---

# Notes

- `team2_publisher.py` simulates Team 2 by publishing findings.
- `team4_subscriber.py` simulates Team 4 by receiving processed risk assessments.
- `finding_service.py` contains the reusable business logic for processing findings.
- `findings.py` and `risks.py` are **development/testing APIs** and are **not part of the production workflow**.
- The production workflow is fully **event-driven** using NATS messaging.
- Every message received from Team 2 automatically creates:
  - One record in the `findings` table.
  - One record in the `risk_assessments` table.
- Team 4 receives processed results on the `team3.risk.assessed` subject.

---

# Requirements

- Python 3.13+
- PostgreSQL
- NATS Server
- FastAPI
- SQLAlchemy
- Pydantic v2
- Uvicorn
