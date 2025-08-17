
import schedule
import time
from news_fetcher import fetch_news
from summarizer import summarize_news

def daily_news_job():
    """Fetch, summarize, and print daily news"""
    news = fetch_news()
    summaries = summarize_news(news[:5])  # summarize top 5 articles
    print("\n🔔 Daily News Summary 🔔")
    for i, s in enumerate(summaries, 1):
        print(f"{i}. {s}")

def start_notifier():
    """Run a daily notifier"""
    schedule.every().day.at("09:00").do(daily_news_job)
    while True:
        schedule.run_pending()
        time.sleep(60)
