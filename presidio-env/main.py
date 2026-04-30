from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from engine import scrub_pii
import time
import logging

# Setup basic logging to console
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

app = FastAPI(
    title="Secure-Link Governance Gateway",
    description="A production-ready API to audit and sanitize PII from GenAI prompts."
)

# Define the Data Schema with an Example for the UI
class AuditRequest(BaseModel):
    text: str = Field(
        ..., 
        description="The document text to be audited for PII.",
        examples=["My name is Zubair and my phone number is 555-0199"]
    )

@app.post("/audit")
async def audit_text(payload: AuditRequest):
    start_time = time.time()
    
    # Process the text using the logic from engine.py
    clean_text, pii_count = scrub_pii(payload.text)
    
    latency = time.time() - start_time
    
    # Log metrics for AIOps monitoring
    logging.info(f"Audit Complete | PII Caught: {pii_count} | Latency: {latency:.4f}s")
    
    return {
        "status": "success",
        "governance_metrics": {
            "pii_entities_detected": pii_count,
            "latency_seconds": latency
        },
        "sanitized_data": clean_text
    }