from flask import Blueprint, render_template, request, flash
from app.news_api import fetch_news
from app.twitter_api import fetch_tweets
from app.content_generator import generate_content

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    print("Route / accessed")
    content = None
    error = None
    if request.method == 'POST':
        print("POST request received")
        tags = request.form.get('tags')
        if not tags:
            flash('Please enter at least one tag.', 'error')
        else:
            try:
                print("Fetching news articles...")
                news_articles = fetch_news(tags)
                if news_articles is None:
                    raise Exception("Failed to fetch news articles.")
                print("News articles fetched")

                print("Fetching tweets...")
                tweets = fetch_tweets(tags)
                if tweets is None:
                    raise Exception("Failed to fetch tweets.")
                print("Tweets fetched")

                print("Generating content...")
                content = generate_content(news_articles, tweets)
                if not content:
                    raise Exception("Failed to generate content.")
                print("Content generated")
            except Exception as e:
                error = str(e)
                print(f"Error: {error}")
                flash('An error occurred while generating content. Please try again.', 'error')
    
    return render_template('index.html', content=content, error=error)
