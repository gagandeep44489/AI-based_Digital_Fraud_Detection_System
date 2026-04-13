from pydantic import BaseModel, HttpUrl


class URLCheckRequest(BaseModel):
    url: HttpUrl


class URLCheckResponse(BaseModel):
    url: str
    is_suspicious: bool
    risk_score: int
    explanation: str
