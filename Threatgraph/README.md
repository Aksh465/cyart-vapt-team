# ThreatGraph - Team 3 Vulnerability & Risk Assessment Engine

ThreatGraph Team 3 is responsible for receiving findings from Team 2, enriching vulnerabilities using public threat intelligence, calculating risk scores, storing results, and publishing risk assessments to Team 4.

---

# Architecture

```
                  +--------------------+
                  |      Team 2        |
                  | Asset Findings     |
                  +---------+----------+
                            |
                            | NATS
                            v
                team2.findings Subject
                            |
                            v
          +--------------------------------+
          | Team 3 Risk Assessment Engine  |
          +--------------------------------+
          |                                |
          | 1. Receive Finding             |
          | 2. Check Vulnerability Cache   |
          | 3. Local Knowledge Base        |
          | 4. Internet Search (Fallback)  |
          | 5. Fetch CVSS from NVD         |
          | 6. Fetch EPSS Score            |
          | 7. Calculate Risk              |
          | 8. Store in PostgreSQL         |
          | 9. Publish to Team 4           |
          +--------------------------------+
                            |
                            | NATS
                            v
           team3.risk.assessed Subject
                            |
                            v
                  +---------------------+
                  |      Team 4         |
                  | Alert / Dashboard   |
                  +---------------------+
```

---

# Features

- FastAPI REST API
- PostgreSQL Database
- SQLAlchemy ORM
- NATS Messaging
- CVE Identification
- Vulnerability Enrichment
- NVD Integration
- EPSS Integration
- Vulnerability Cache
- Risk Scoring Engine
- Team 2 → Team 3 → Team 4 Workflow

---

# Project Structure

```
app
│
├── api
│   ├── findings.py
│   ├── risks.py
│   └── dashboard.py
│
├── core
│   ├── config.py
│   └── database.py
│
├── models
│   ├── finding.py
│   ├── risk_assessment.py
│   └── vulnerability_cache.py
│
├── schemas
│
├── services
│   ├── finding_service.py
│   ├── nats_publisher.py
│   ├── nats_subscriber.py
│   ├── risk_scoring.py
│   └── vulnerability_enrichment.py
│
├── team2_publisher.py
├── team4_subscriber.py
├── create_tables.py
└── main.py
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ThreatGraph.git

cd ThreatGraph
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL

Create database

```
threatgraph
```

Update `.env`

```env
APP_NAME=ThreatGraph

SECRET_KEY=your_secret_key

ALGORITHM=HS256

DATABASE_URL=postgresql://postgres:password@localhost/threatgraph

NATS_URL=nats://localhost:4222

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Create Database Tables

Run

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

Expected

```
Listening on 0.0.0.0:4222
```

---

# Run Team 3

Start FastAPI

```bash
uvicorn app.main:app --reload
```

Expected

```
Application startup complete

NATS Subscriber Started

Listening on subject:

team2.findings
```

---

# Run Team 4

Open another terminal

```bash
python app/team4_subscriber.py
```

Expected

```
Connected Successfully

Waiting for Risk Assessments...
```

---

# Run Team 2

Open another terminal

```bash
python app/team2_publisher.py
```

Team 2 publishes findings.

---

# Workflow

## Step 1

Team 2 publishes

```
Title

Hostname

Severity

Exposure

Exploit Available

Status
```

Example

```json
{
    "asset_id":101,
    "hostname":"web-prod-01",
    "title":"Apache Log4j Remote Code Execution",
    "severity":"Critical",
    "exposure_context":"Internet-facing",
    "exploit_available":true,
    "status":"OPEN"
}
```

---

## Step 2

Team 3 receives finding.

```
Received Finding
```

---

## Step 3

Check Vulnerability Cache

If cached

```
Use Cached Data
```

Else

```
Continue
```

---

## Step 4

Search Local Knowledge Base

If found

```
Use Local Mapping
```

Else

```
Search Internet (NVD Keyword Search)
```

---

## Step 5

Fetch Threat Intelligence

Team 3 downloads

- CVE ID
- CVSS Score
- EPSS Score

using

- NVD API
- FIRST EPSS API

---

## Step 6

Store into Cache

Future requests use cached data.

No additional API calls are required.

---

## Step 7

Calculate Risk

Formula

```
Base Score = CVSS × 10

Exploit Likelihood = EPSS × 100

KEV Multiplier

×

Asset Criticality

×

Exposure Context

÷

Normalization Factor
```

Priority

```
75 - 100

CRITICAL

50 - 74

HIGH

25 - 49

MEDIUM

0 - 24

LOW
```

---

## Step 8

Store

Finding

Risk Assessment

---

## Step 9

Publish to Team 4

Published subject

```
team3.risk.assessed
```

---

# APIs

Swagger

```
http://127.0.0.1:8000/docs
```

---

# Development APIs

These endpoints are **only for development and testing**.

```
GET /findings/demo
```

Creates a sample finding and calculates a risk assessment.

```
POST /risk/calculate/{finding_id}
```

Calculates a risk assessment for an existing finding.

> These APIs are **not part of the Team 2 → Team 3 → Team 4 production workflow**.

---

# Production Workflow

The production workflow uses **NATS messaging** instead of the development APIs.

```
Team 2
↓

team2_publisher.py

↓

NATS

↓

Team 3

↓

FastAPI Subscriber

↓

Threat Intelligence

↓

Risk Calculation

↓

PostgreSQL

↓

NATS

↓

Team 4

↓

team4_subscriber.py
```

---

# External APIs Used

NVD

```
https://services.nvd.nist.gov/rest/json/cves/2.0
```

FIRST EPSS

```
https://api.first.org/data/v1/epss
```

---

# Technologies

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- NATS
- Requests
- Pydantic
- NVD API
- FIRST EPSS API

---

# Team Responsibilities

### Team 3

- CVE Identification
- Vulnerability Enrichment
- Risk Assessment
- Risk Prioritization
- Threat Intelligence
- Publish Risk Assessment
