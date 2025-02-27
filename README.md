# AI Web Analyser

### **AI System for Sacanning the Web**

![Project Banner](./assets/project_image_1.png)

## Overview
AI Web Analyser is an advanced AI-powered tool that scans, summarises, and evaluates the credibility of online articles. It extracts key insights, detects biases, and provides reliability assessments, offering a valuable solution for researchers, journalists, and the general public to discern factual information from misinformation.

## Features
- **AI-Powered Summarisation** – Uses NLP models to generate concise summaries of web articles.
- **Credibility Analysis** – Evaluates the reliability of sources using AI-driven fact-checking mechanisms.
- **Web Scraping** – Extracts clean textual data from URLs while removing irrelevant elements such as ads and scripts.
- **Bias Detection** – Analyses sentiment and potential political or emotional biases within the content.
- **Interactive User Interface** – Built using Gradio for an intuitive and user-friendly experience.

## Technology Stack
- **Python 3.11** – Core programming language.
- **FastAPI** – Provides an efficient and scalable API backend.
- **BeautifulSoup** – Extracts and cleans webpage text.
- **Hugging Face Transformers** – Leverages NLP models for summarisation and analysis.
- **Gradio** – Enables an interactive web-based interface.
- **Docker** – Containerisation for deployment.

## Project Structure
```
ai-web-analyser
├── app/
│   ├── main.py        # FastAPI backend
│   ├── summariser.py  # AI summarisation logic
│   ├── credibility.py # Fake news detection
├── ui/
│   ├── gradio_ui.py   # User interface (Gradio)
├── utils/
│   ├── scraper.py     # Web scraping utilities
├── tests/
│   ├── test_app.py    # Unit tests
├── deployment/
│   ├── Dockerfile     # Deployment setup
│   ├── requirements.txt
├── README.md
├── assets/
│   ├── project_image.png  # AI-generated image
```

## Installation & Usage
### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-web-analyser.git
cd ai-web-analyser
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API
```bash
uvicorn app.main:app --reload
```

### 4. Open Gradio UI
```bash
python ui/gradio_ui.py
```

## Contribution Guidelines
Contributions are welcome. Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Make your changes and commit them.
4. Submit a pull request.

## License
This project is licensed under the **MIT License** – you are free to use, modify, and distribute it.

