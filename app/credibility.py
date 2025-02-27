from transformers import pipeline

classifier = pipeline("text-classification", model="facebook/bart-large-mnli")

def assess_credibility(url):
    categories = ["credible", "misinformation", "satire"]
    result = classifier(url, candidate_labels=categories)
    return max(zip(result["labels"], result["scores"]), key=lambda x: x[1])[0]
