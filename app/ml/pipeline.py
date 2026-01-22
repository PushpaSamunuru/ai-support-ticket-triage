from transformers import pipeline

# Zero-shot: categorize ticket into one of these labels
INTENT_LABELS = ["billing", "bug", "outage", "feature_request", "account", "other"]

zero_shot = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

RISK_KEYWORDS = ["refund", "chargeback", "lawsuit", "legal", "scam", "fraud", "hate", "kill"]

def predict_intent(text: str):
    result = zero_shot(text, INTENT_LABELS)
    label = result["labels"][0]
    score = float(result["scores"][0])
    return label, score

def detect_risk(text: str):
    t = text.lower()
    for kw in RISK_KEYWORDS:
        if kw in t:
            return "yes"
    return "no"
