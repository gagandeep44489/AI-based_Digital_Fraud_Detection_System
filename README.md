# AI-powered Digital Fraud Detection Platform for preventing scams in India

> A startup-ready full-stack project that helps users detect scam messages (SMS, WhatsApp, job offers, links) in seconds.

## Problem Statement
India faces a growing number of digital fraud cases through fake job offers, phishing links, urgent payment requests, and social engineering messages. Most users struggle to quickly judge whether a message is safe or a scam.

## Solution Overview
This platform provides a simple interface where users submit suspicious content and get:
- Scam/Safe prediction
- Confidence score
- Fraud category
- Human-readable explanation

It combines a modern web UI with a FastAPI backend, a rule-based fraud detection engine (MVP), and a scalable architecture ready for ML upgrades.

## Features
- JWT Authentication (register/login)
- Message submission and risk scoring
- Prediction retrieval by message ID
- Feedback loop for model improvement
- URL risk checker (HTTP/HTTPS + domain heuristics)
- Rule seeding for default fraud keywords
- React dashboard for easy user interaction
- Deployment-ready setup (Render, AWS EC2, Docker)

## Screenshots (Placeholders)
> Replace these with real product images before investor demos.

- UI Preview: `docs/screenshots/ui-preview-placeholder.md`
- API Docs Preview: `docs/screenshots/api-docs-placeholder.md`

![UI Preview Placeholder](https://via.placeholder.com/1000x500?text=UI+Preview+Placeholder)
![API Docs Placeholder](https://via.placeholder.com/1000x500?text=API+Docs+Placeholder)

## Demo: How It Works
1. User opens frontend and enters suspicious message text.
2. Frontend sends message to backend (`POST /messages`).
3. Backend detection engine checks risky keywords/rules.
4. Prediction is stored and fetched (`GET /predictions/{message_id}`).
5. UI displays result + confidence + explanation.

## Architecture Diagram (Text)
```text
[React Frontend]
      |
      v
[FastAPI API Layer]
      |
      v
[Fraud Detection Engine (Rules now, ML later)]
      |
      v
[PostgreSQL / SQLite Database]
```

## Tech Stack
### Backend
- Python 3.11
- FastAPI
- SQLAlchemy
- JWT Authentication
- PostgreSQL (production) / SQLite (dev)

### Frontend
- React (Vite)
- Tailwind CSS
- Axios

### DevOps
- Docker
- Render deployment
- AWS EC2 + Nginx

## Quick Start (Local)
### 1) Backend
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### 2) Frontend
```bash
npm install
npm run dev
```

### 3) Open
- Frontend: `http://127.0.0.1:5173`
- API Docs: `http://127.0.0.1:8000/docs`

## Demo Instructions
- Submit sample text: `Earn money fast, no skills needed, registration fee required!`
- System should return high-risk/scam prediction with explanation.

## API Endpoints
### Auth
- `POST /auth/register`
- `POST /auth/login`

### Core Fraud Flow
- `POST /messages`
- `GET /predictions/{message_id}`
- `POST /feedback`

### Utility
- `POST /check-url`
- `GET /health`

Detailed endpoint docs: `docs/api_reference.md`

## Documentation
- System Design: `docs/system_design.md`
- API Reference: `docs/api_reference.md`
- Deployment Guide: `DEPLOYMENT.md`

## Roadmap
### Phase 1: MVP (Current)
- Rule-based detection
- Basic user dashboard
- Feedback capture

### Phase 2: ML Intelligence
- Train supervised fraud classifier
- Multi-language support (English + regional Indian languages)
- Better explainability and fraud taxonomy

### Phase 3: Scaling & Enterprise
- Queue-based asynchronous inference
- Model monitoring + drift detection
- Multi-tenant architecture and analytics dashboard

## Impact & Scalability
- Protects users from financial fraud and phishing scams.
- Designed to evolve from keyword rules to robust AI-driven detection.
- Suitable for hackathons, pilot programs, startup demos, and funding decks.

## Contributing
Please read `CONTRIBUTING.md` before submitting pull requests.

## License
This project is licensed under the MIT License. See `LICENSE`.
