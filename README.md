# AI-based Digital Fraud Detection System

This repository contains:
- **FastAPI backend** for fraud detection APIs
- **React + Vite frontend** for a clean user interface

## Backend (FastAPI)
Run with:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Docs: `http://127.0.0.1:8000/docs`

## Frontend (React + Tailwind)
Run with:
```bash
npm install
npm run dev
```

Frontend URL: `http://127.0.0.1:5173`

The frontend calls backend APIs at `http://127.0.0.1:8000`:
- `POST /messages`
- `GET /predictions/{message_id}`

> Note: Backend message endpoints currently require JWT auth. To test quickly, store a valid token in browser localStorage under key `token`.
