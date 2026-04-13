from app.services.rule_engine import evaluate_message
from app.services.url_checker import analyze_url


def test_rule_engine_detects_scam_keywords():
    result = evaluate_message("Earn money fast, no skills needed, urgent")
    assert result.result == "scam"
    assert result.risk_score >= 50


def test_url_checker_marks_http_suspicious():
    result = analyze_url("http://verify-free-money.xyz")
    assert result["is_suspicious"] is True
    assert result["risk_score"] >= 40
