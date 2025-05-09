from fastapi import FastAPI, UploadFile, File
from datetime import datetime

app = FastAPI()

def validate_document(content: str) -> dict:
    required_terms = [
        "Fractal Bindu Shell",
        "Spiral Geodesic",
        "Recursive Structure",
        "Adaptive Scaling",
        "Phase Modulation"
    ]
    findings = []
    for term in required_terms:
        if term in content:
            findings.append(f"Found: {term}")
        else:
            findings.append(f"Missing: {term}")

    status = "Complete" if all("Found" in f for f in findings) else "Incomplete"
    recommendations = "No action needed." if status == "Complete" else "Please review missing elements."
    return {
        "status": status,
        "findings": findings,
        "recommendations": recommendations,
        "report_generated_at": datetime.utcnow().isoformat()
    }

@app.post("/validate")
async def validate(file: UploadFile = File(...)):
    content = await file.read()
    content_text = content.decode("utf-8", errors="ignore")
    report = validate_document(content_text)
    return report