from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.db.database import SessionLocal, engine, Base
from app.models import Ticket
from app.services.triage import triage

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

CONF_THRESHOLD = 0.70

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    db = SessionLocal()
    tickets = db.query(Ticket).order_by(Ticket.created_at.desc()).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "tickets": tickets})

@app.post("/submit")
def submit_ticket(title: str = Form(...), description: str = Form(...)):
    result = triage(description)

    status = "open"
    if result["intent_conf"] < CONF_THRESHOLD:
        status = "review"

    db = SessionLocal()
    ticket = Ticket(
        title=title,
        description=description,
        intent=result["intent"],
        intent_confidence=result["intent_conf"],
        urgency=result["urgency"],
        urgency_confidence=result["urgency_conf"],
        risky=result["risky"],
        suggested_reply=result["suggested_reply"],
        status=status
    )
    db.add(ticket)
    db.commit()
    db.close()

    return RedirectResponse(url="/", status_code=303)

@app.get("/ticket/{ticket_id}", response_class=HTMLResponse)
def view_ticket(request: Request, ticket_id: int):
    db = SessionLocal()
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    db.close()
    return templates.TemplateResponse("ticket.html", {"request": request, "ticket": ticket})

@app.post("/ticket/{ticket_id}/override")
def override_ticket(
    ticket_id: int,
    intent: str = Form(...),
    urgency: str = Form(...),
    status: str = Form(...),
):
    db = SessionLocal()
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    ticket.intent = intent
    ticket.urgency = urgency
    ticket.status = status
    ticket.human_override = "yes"
    db.commit()
    db.close()
    return RedirectResponse(url=f"/ticket/{ticket_id}", status_code=303)
