import requests
from config import NEWS_API_URL, API_KEY, COUNTRY, CATEGORY

def fetch_news():
    """Fetch latest news from API"""
    params = {
        "country": COUNTRY,
        "category": CATEGORY,
        "apiKey": API_KEY
    }
    response = requests.get(NEWS_API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        return [article["title"] + " - " + article.get("description", "") for article in articles]
    else:
        return ["Error fetching news"]
