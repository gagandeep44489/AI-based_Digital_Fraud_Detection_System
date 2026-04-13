import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.config import get_settings
from app.database import Base, SessionLocal, engine
from app.models.rule import Rule
from app.routes import auth, feedback, messages, predictions, url_checker

settings = get_settings()
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(messages.router)
app.include_router(predictions.router)
app.include_router(feedback.router)
app.include_router(url_checker.router)


def seed_default_rules(db: Session) -> None:
    defaults = [
        ("earn money", "job_scam", 30, "Promises easy or unrealistic income"),
        ("registration fee", "job_scam", 35, "Requests upfront payment to join"),
        ("no skills", "job_scam", 20, "Claims no experience or skills needed"),
        ("urgent", "general", 15, "Pressures user with urgency"),
    ]

    for keyword, category, weight, description in defaults:
        exists = db.query(Rule).filter(Rule.keyword == keyword).first()
        if not exists:
            db.add(Rule(keyword=keyword, category=category, weight=weight, description=description))

    db.commit()


@app.on_event("startup")
def startup_event() -> None:
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        seed_default_rules(db)
    logger.info("Application started and database initialized")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
