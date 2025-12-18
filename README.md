# 🏈🏀⚾ Fantasy Sports API & Analytics Platform
Author:
Taylor Poe

### A production-style Fantasy Sports backend platform that aggregates real sports data, normalizes it into a fantasy-ready schema, and calculates fantasy scoring using asynchronous background processing.

### This project was built to demonstrate backend system design, API integration, data modeling, and scalable job pipelines — using patterns similar to real fantasy platforms.

## 🔗 LinkedIn: https://www.linkedin.com/in/tpoe25

## 🔗 GitHub: https://github.com/TPoe25

### What This Project Does
- Ingests real sports data from free public APIs
- Normalizes players, teams, and stats into PostgreSQL
- Calculates Yahoo-style fantasy scoring programmatically
- Uses Celery + Redis for asynchronous jobs
- Designed to scale and swap data providers easily
- Deployed using Render with cloud-ready configuration

### Architecture Overview
```mermaid
Client / Cron
     |
     v
Flask REST API
     |
     v
Service Layer (API adapters)
     |
     v
Celery Workers (async jobs)
     |
     v
PostgreSQL (normalized data)
```

## Key design choices
- Flask for clarity and control
- SQLAlchemy ORM (no raw SQL)
- Celery for non-blocking background work
- PostgreSQL for structured, queryable data
- External APIs isolated behind service adapters

## Tech Stack
```
- Python 3
- Flask
- SQLAlchemy
- Celery + Redis
- PostgreSQL
- Render (cloud deployment)
```

## Sports Data Sources (Free)

```NFL: ESPN public JSON feeds (unofficial, wrapped for safety)```

```NBA: balldontlie (free tier)```

```MLB: MLB Stats API (public endpoints)```

- The system is built so licensed or paid APIs can be swapped in later without changing core logic.

## Fantasy Scoring

### Fantasy scoring is calculated centrally using configurable, Yahoo-style rules.

**Examples**:
```
NFL: passing yards, TDs, interceptions, PPR

NBA: points, rebounds, assists, steals, blocks

MLB: home runs, RBI, runs, strikeouts
```
Scoring logic is abstracted so different league formats can be supported.

## Asynchronous Processing
- Background workers handle:
- data ingestion and normalization
- fantasy scoring calculations
- scheduled sync jobs

## ML inference (image classification extension)

This mirrors how real production systems handle heavy workloads.

## **Running Locally**
```
pip install -r requirements.txt
cp .env.example .env
redis-server
python run.py
celery -A celery_worker.celery worker --loglevel=info
```
## Why This Project Matters

### This project demonstrates my ability to:
- design backend systems around real data
- work with external and unstable APIs
- model relational data correctly
- build async job pipelines
- deploy and operate cloud-based services

It reflects how I approach real engineering problems: build something that works now, but is designed to scale.
