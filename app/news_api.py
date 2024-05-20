import requests
from app.config import GOOGLE_NEWS_API_KEY

def fetch_news(query):
    try:
        url = f'https://newsapi.org/v2/everything?q={query}&apiKey={GOOGLE_NEWS_API_KEY}'
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Google News API error: {e}")
        return None

if __name__ == '__main__':
    query = 'technology'
    news_data = fetch_news(query)
    if news_data:
        print(news_data)
