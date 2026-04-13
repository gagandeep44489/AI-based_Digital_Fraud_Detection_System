# System Design

## Overview
The platform is designed as a modular full-stack system for fraud-risk detection.

## High-Level Architecture
```text
[Web Client (React)]
        |
        v
[FastAPI Backend]
        |
        +--> [Auth Service (JWT)]
        +--> [Fraud Detection Service]
        +--> [URL Checker Service]
        |
        v
[Database: PostgreSQL/SQLite]
```

## Core Components
1. **Frontend**
   - Message input and result visualization.
2. **API Layer**
   - Validates requests and orchestrates services.
3. **Detection Engine**
   - Rule-based scoring today, ML-ready extension point.
4. **Persistence Layer**
   - Stores users, messages, predictions, feedback, and rules.

## Scalability Direction
- Move inference to async workers.
- Add caching for repeated URL checks.
- Add observability (metrics, logs, tracing).
- Switch SQLite to managed PostgreSQL in production.
