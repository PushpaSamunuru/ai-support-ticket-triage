from app.ml.pipeline import predict_intent, detect_risk

def predict_urgency(text: str):
    t = text.lower()
    if "down" in t or "outage" in t or "not working" in t:
        return "high", 0.85
    if "refund" in t or "charged" in t or "urgent" in t:
        return "medium", 0.75
    return "low", 0.65

def suggest_reply(intent: str):
    templates = {
        "billing": "Sorry about the billing issue. Please share your invoice ID and the last 4 digits of your card. We will investigate immediately.",
        "bug": "Thanks for reporting this. Please share steps to reproduce, expected behavior, and screenshots/logs if possible.",
        "outage": "We’re investigating the outage right now. Can you confirm your region and the exact error message/time?",
        "feature_request": "Thanks for the suggestion! Please share your use case and why it would help your workflow.",
        "account": "I can help with your account issue. Please confirm the email on the account and what you tried so far.",
        "other": "Thanks for reaching out. Please provide a bit more detail so we can route this correctly."
    }
    return templates.get(intent, templates["other"])

def triage(text: str):
    intent, intent_conf = predict_intent(text)
    urgency, urg_conf = predict_urgency(text)
    risky = detect_risk(text)
    reply = suggest_reply(intent)
    return {
        "intent": intent,
        "intent_conf": intent_conf,
        "urgency": urgency,
        "urgency_conf": urg_conf,
        "risky": risky,
        "suggested_reply": reply
    }
