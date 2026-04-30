from fastapi import FastAPI, HTTPException
from engine import scrub_pii
import time
import logging

app = FastAPI(title="Secure-Link Governance Gateway")

@app.post("/audit")
async def audit_text(payload: dict):
    start_time = time.time()
    text = payload.get("text")
    
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    # The actual Governance call
    clean_text, pii_count = scrub_pii(text)
    
    latency = time.time() - start_time
    
    # Logic to log the "AIOps" metrics
    logging.info(f"Audit Complete | PII Caught: {pii_count} | Latency: {latency:.4f}s")
    
    return {
        "status": "success",
        "governance_metrics": {
            "pii_entities_detected": pii_count,
            "latency_seconds": latency
        },
        "sanitized_data": clean_text
    }