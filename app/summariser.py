import requests
from bs4 import BeautifulSoup
from transformers import pipeline

summariser = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return " ".join([p.text for p in soup.find_all("p")])

def generate_summary(url):
    text = extract_text(url)
    return summariser(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
