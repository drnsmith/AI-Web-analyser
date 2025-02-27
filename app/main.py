from fastapi import FastAPI
from app.summariser import generate_summary
from app.credibility import assess_credibility

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AI Web Analyser"}

@app.post("/summarise/")
def summarise_article(url: str):
    summary = generate_summary(url)
    credibility = assess_credibility(url)
    return {"summary": summary, "credibility": credibility}
