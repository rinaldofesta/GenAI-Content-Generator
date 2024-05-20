import secrets

GOOGLE_NEWS_API_KEY = 'your_google_news_api_key'
TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET_KEY = 'your_twitter_api_secret_key'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'
OPENAI_API_KEY = 'your_openai_api_key'

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

SECRET_KEY = secrets.token_hex(16)  # Generates a random 32-character hex string

DEBUG = True
TESTING = True
ALLOWED_HOSTS = ['*']
