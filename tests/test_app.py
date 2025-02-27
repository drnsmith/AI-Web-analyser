from app.summariser import generate_summary

def test_summary():
    text = "This is a test article with relevant content."
    summary = generate_summary(text)
    assert isinstance(summary, str)
    assert len(summary) > 10
