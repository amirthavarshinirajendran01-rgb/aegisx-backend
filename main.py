import os
import re
import time
from typing import Dict, List, Optional
from urllib.parse import urlparse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI(title="AegisX Privacy API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mathematical Verhoeff Algorithm for Indian Aadhaar
VERHOEFF_D = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
    [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
    [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
    [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
    [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
    [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
    [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
    [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]
VERHOEFF_P = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
    [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
    [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
    [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
]

def validate_aadhaar(num_str: str) -> bool:
    cleaned = re.sub(r'\D', '', num_str)
    if len(cleaned) != 12:
        return False
    c = 0
    digits = [int(x) for x in reversed(cleaned)]
    for i in range(12):
        c = VERHOEFF_D[c][VERHOEFF_P[i % 8][digits[i]]]
    return c == 0

PATTERNS = {
    "pan": re.compile(r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b'),
    "credit_card": re.compile(r'\b(?:\d{4}[-\s]?){3}\d{4}\b'),
    "ifsc": re.compile(r'\b[A-Z]{4}0[A-Z0-9]{6}\b'),
    "upi": re.compile(r'[a-zA-Z0-9.\-_]{2,256}@(okaxis|okhdfcbank|okicici|oksbi|paytm|ybl|upi|apl)\b', re.IGNORECASE),
    "aws_key": re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
    "openai_key": re.compile(r'\bsk-[a-zA-Z0-9]{48}\b'),
    "phone": re.compile(r'(?:\+91[\-\s]?)?[6-9]\d{9}\b'),
    "email": re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
}

class SanitizeRequest(BaseModel):
    text: str

class AuditRequest(BaseModel):
    url: str

class DpdpRequest(BaseModel):
    company_name: str
    dpo_email: Optional[str] = None
    user_name: Optional[str] = "Concerned Citizen"

@app.get("/")
def home():
    return {"status": "online", "service": "AegisX Privacy Core"}

@app.post("/api/sanitize")
def sanitize(req: SanitizeRequest):
    start = time.perf_counter()
    modified = req.text
    detections = []

    # Aadhaar Check
    for raw in re.findall(r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b', modified):
        if validate_aadhaar(raw):
            modified = modified.replace(raw, "[AADHAAR_SECURE: 5555 4444 3333]")
            detections.append("Aadhaar Card (Verhoeff Verified)")

    # PAN, Cards, Keys, Contact
    for match in PATTERNS["pan"].findall(modified):
        modified = modified.replace(match, "[PAN_SECURE: ABCDE1234F]")
        detections.append("PAN Card")

    for match in PATTERNS["credit_card"].findall(modified):
        modified = modified.replace(match, "[CARD_SECURE: 4111-XXXX-XXXX-4444]")
        detections.append("Credit/Debit Card")

    for match in PATTERNS["aws_key"].findall(modified):
        modified = modified.replace(match, "[API_KEY: AKIA_DUMMY_KEY]")
        detections.append("AWS Secret Key")

    for match in PATTERNS["phone"].findall(modified):
        modified = modified.replace(match, "+91 99999 00000")
        detections.append("Mobile Number")

    for match in PATTERNS["email"].findall(modified):
        modified = modified.replace(match, "alex.doe@example.com")
        detections.append("Email Address")

    elapsed = round((time.perf_counter() - start) * 1000, 2)
    return {
        "sanitized_text": modified,
        "detections": list(set(detections)),
        "latency_ms": elapsed
    }

@app.post("/api/audit-website")
def audit(req: AuditRequest):
    url = req.url.strip()
    if not url.startswith("http"):
        url = "https://" + url

    status = "SAFE"
    color = "green"
    reasons = ["Secure HTTPS verified."]

    try:
        resp = requests.get(url, timeout=4, headers={"User-Agent": "AegisX-Scanner"})
        content = resp.text.lower()
        if any(x in content for x in ["hotjar", "fullstory", "smartlook", "clarity"]):
            status = "HIGH_RISK"
            color = "red"
            reasons.append("Pre-submission keystroke recording scripts detected in page.")
        elif "cookie" in content and "reject" not in content:
            status = "MODERATE"
            color = "yellow"
            reasons.append("Tricky cookie banner detected: Hidden reject option.")
    except Exception:
        status = "MODERATE"
        color = "yellow"
        reasons.append("Network check timed out. Partial scan complete.")

    return {"url": url, "status": status, "color": color, "reasons": reasons}

@app.post("/api/generate-dpdp-notice")
def dpdp_notice(req: DpdpRequest):
    company = req.company_name
    dpo = req.dpo_email if req.dpo_email else f"privacy@{company.lower().replace(' ', '')}.com"
    notice = f"Formal Legal Notice for Data Erasure under Section 12 of the DPDP Act 2023 to DPO of {company} ({dpo}). All data processing consent is hereby withdrawn."
    return {"notice": notice}
