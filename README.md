# AI-based Digital Fraud Detection System (Backend)

Production-style FastAPI backend for fraud risk detection over suspicious messages and URLs.

## Features
- JWT Authentication (`/auth/register`, `/auth/login`)
- Message ingestion + automatic fraud prediction (`/messages`)
- Prediction retrieval (`/predictions/{message_id}`)
- User feedback capture (`/feedback`)
- URL safety checker (`/check-url`)
- Rule seeding on startup (`rules` table)

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Open docs: `http://127.0.0.1:8000/docs`
