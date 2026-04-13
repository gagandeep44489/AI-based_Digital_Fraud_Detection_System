from fastapi import APIRouter

from app.schemas.url_checker import URLCheckRequest, URLCheckResponse
from app.services.url_checker import analyze_url

router = APIRouter(tags=["URL Checker"])


@router.post("/check-url", response_model=URLCheckResponse)
def check_url(payload: URLCheckRequest) -> URLCheckResponse:
    return URLCheckResponse(**analyze_url(str(payload.url)))
