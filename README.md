# AI Support Ticket Triage System (NLP)

A practical AI/ML product that auto-triages support tickets:
- Classifies **intent** (Billing / Bug / Outage / Feature Request / Account / Security)
- Predicts **urgency**
- Flags **risky language** (angry / threat / escalation keywords)
- Shows **confidence scores** so humans can override safely

Built to reflect how ML is shipped inside real systems (API + DB + UI), not just notebooks.

---

## Demo Outputs (Screenshots)


<img width="1920" height="1080" alt="Screenshot 2026-01-22 154656" src="https://github.com/user-attachments/assets/3440a2cd-498e-4a03-ad1f-45dbd1e0939a" />


<img width="1920" height="1080" alt="Screenshot 2026-01-22 154702" src="https://github.com/user-attachments/assets/850a3f04-09a8-45b9-93f3-ffb1200d7448" />

---

## Tech Stack
- **API:** FastAPI
- **Server:** Uvicorn
- **DB:** SQLite + SQLAlchemy
- **ML/NLP:** HuggingFace Transformers (text classification)
- **UI:** Simple HTML/Jinja (or your UI approach)

---

## Setup (Windows / Conda)

### 1) Create environment
```bash
conda create -n triage39 python=3.9 -y
conda activate triage39

2) Install dependencies
pip install -r requirements.txt

3) Run the app
uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000

Example Tickets to Test
Ticket A — Urgent / Outage

Title: Checkout failing for multiple users
Description: Payments fail with error 502 on checkout. This is impacting revenue and customers are complaining.

Ticket B — Security Concern

Title: Suspicious login attempts
Description: I’m seeing login attempts from unknown locations. Please lock my account and investigate immediately.


