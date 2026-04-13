from dataclasses import dataclass


@dataclass
class RuleMatchResult:
    risk_score: int
    result: str
    confidence: float
    category: str
    explanation: str


DEFAULT_RULES = {
    "earn money": 30,
    "registration fee": 35,
    "no skills": 20,
    "urgent": 15,
}


def evaluate_message(content: str, rules: dict[str, int] | None = None) -> RuleMatchResult:
    normalized = content.lower()
    active_rules = rules or DEFAULT_RULES

    matched = [keyword for keyword in active_rules if keyword in normalized]
    raw_score = sum(active_rules[keyword] for keyword in matched)
    risk_score = min(raw_score, 100)

    result = "scam" if risk_score >= 50 else "safe"
    confidence = max(0.50, min(0.99, risk_score / 100 if result == "scam" else 1 - (risk_score / 120)))
    category = "job_scam" if any(k in matched for k in {"earn money", "registration fee", "no skills"}) else "general"

    if matched:
        explanation = f"Contains suspicious keywords: {', '.join(matched)}"
    else:
        explanation = "No suspicious keyword patterns detected"

    return RuleMatchResult(
        risk_score=risk_score,
        result=result,
        confidence=round(confidence, 2),
        category=category,
        explanation=explanation,
    )
