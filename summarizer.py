from transformers import pipeline

# Using HuggingFace summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_news(news_list):
    """Summarize a list of news articles"""
    summaries = []
    for article in news_list:
        try:
            summary = summarizer(article, max_length=50, min_length=25, do_sample=False)
            summaries.append(summary[0]["summary_text"])
        except Exception as e:
            summaries.append("Error summarizing article")
    return summaries
