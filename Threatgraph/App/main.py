from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio

from app.api.findings import router as findings_router
from app.api.risks import router as risks_router
from app.api.dashboard import router as dashboard_router

from app.services.nats_subscriber import start_subscriber

app = FastAPI(
    title="ThreatGraph Risk Assessment",
    version="0.1.0"
)

# Include APIs
app.include_router(findings_router)
app.include_router(risks_router)
app.include_router(dashboard_router)

# Static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_subscriber())
    print("NATS Subscriber Started")


# Dashboard
@app.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
