from app import create_app
from app.news_api import fetch_news
from app.twitter_api import fetch_tweets
from app.content_generator import generate_content
from app.celery import make_celery

app = create_app()
celery = make_celery(app)

@celery.task
def update_content():
    tags = 'technology, AI'  # Default tags
    news_articles = fetch_news(tags)
    tweets = fetch_tweets(tags)
    content = generate_content(news_articles, tweets)
    # Store or publish the content

if __name__ == '__main__':
    update_content.apply_async(countdown=60)  # Example of scheduling a task
