from urllib.parse import urlparse

SUSPICIOUS_TLDS = {".xyz", ".click", ".top", ".work"}
SUSPICIOUS_TERMS = {"verify", "login", "update", "wallet", "bonus", "free-money"}


def analyze_url(url: str) -> dict:
    parsed = urlparse(url)
    hostname = (parsed.hostname or "").lower()

    score = 0
    reasons: list[str] = []

    if parsed.scheme != "https":
        score += 35
        reasons.append("Uses insecure HTTP instead of HTTPS")

    if any(hostname.endswith(tld) for tld in SUSPICIOUS_TLDS):
        score += 30
        reasons.append("Domain uses suspicious top-level domain")

    if any(term in hostname for term in SUSPICIOUS_TERMS):
        score += 20
        reasons.append("Domain contains phishing-like terms")

    if hostname.count("-") >= 3:
        score += 15
        reasons.append("Domain contains many hyphens")

    risk_score = min(score, 100)
    explanation = "; ".join(reasons) if reasons else "No obvious URL red flags detected"

    return {
        "url": url,
        "is_suspicious": risk_score >= 40,
        "risk_score": risk_score,
        "explanation": explanation,
    }
