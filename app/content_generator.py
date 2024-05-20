import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_content(news_articles, tweets):
    try:
        news_content = "\n".join([article['title'] + ": " + article['description'] for article in news_articles['articles']])
        tweet_content = "\n".join(tweets)
        prompt = f"Write a blog post based on the following news and tweets.\n\nNews Articles:\n{news_content}\n\nTweets:\n{tweet_content}\n\nBlog Post:"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Error generating content"

if __name__ == '__main__':
    news_articles = {'articles': [{'title': 'Sample News', 'description': 'Sample Description'}]}
    tweets = ['Sample Tweet']
    content = generate_content(news_articles, tweets)
    print(content)
