from fastapi import FastAPI
import asyncio

from app.api.findings import router as findings_router
from app.api.risks import router as risks_router

from app.services.nats_subscriber import start_subscriber

app = FastAPI(
    title="ThreatGraph Risk Assessment",
    version="0.1.0"
)

app.include_router(findings_router)
app.include_router(risks_router)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_subscriber())
    print("NATS Subscriber Started")


@app.get("/")
def home():
    return {
        "message": "ThreatGraph Running"
    }
