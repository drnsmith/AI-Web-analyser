import gradio as gr
from app.summariser import generate_summary
from app.credibility import assess_credibility

def process_url(url):
    summary = generate_summary(url)
    credibility = assess_credibility(url)
    return summary, credibility

iface = gr.Interface(
    fn=process_url,
    inputs=gr.Textbox(label="Enter URL"),
    outputs=[gr.Textbox(label="Summary"), gr.Textbox(label="Credibility")],
    title="AI Web Analyser",
)

iface.launch()
