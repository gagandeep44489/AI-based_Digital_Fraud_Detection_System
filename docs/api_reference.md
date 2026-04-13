# API Reference

Base URL (local): `http://127.0.0.1:8000`

## Authentication
### POST `/auth/register`
Create account and receive JWT token.

### POST `/auth/login`
Login and receive JWT token.

## Message & Prediction
### POST `/messages`
Submit message content and source.

Example request:
```json
{
  "content": "Earn ₹5000 daily, no skills needed",
  "source": "whatsapp"
}
```

### GET `/predictions/{message_id}`
Fetch prediction for stored message.

Example response:
```json
{
  "result": "scam",
  "confidence": 0.85,
  "category": "job_scam",
  "explanation": "Contains suspicious keywords"
}
```

## Feedback
### POST `/feedback`
Mark prediction as correct/incorrect for future ML training.

## URL Checker
### POST `/check-url`
Analyze URL for suspicious signals.

## Health
### GET `/health`
Simple status check endpoint.
