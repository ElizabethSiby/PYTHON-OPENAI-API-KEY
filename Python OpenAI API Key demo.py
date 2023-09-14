import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = ''

def analyze_sentiment(tweet_text):
    openai.api_key = api_key

    # Specify the prompt for sentiment analysis
    prompt = f"Analyze the sentiment of the following tweet: '{tweet_text}'\nSentiment:"

    # Use the OpenAI GPT-3 model to analyze sentiment
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=10
    )

    sentiment = response.choices[0].text.strip()

    return sentiment

if __name__ == "__main__":
    # List of example tweets
    tweets = [
        "I'm having a great day!",
        "This is the worst weather ever. ",
        "I'm feeling neutral about this.",
        "I can't believe how awesome this is! ",
    ]

    for tweet in tweets:
        sentiment = analyze_sentiment(tweet)
        print(f"Tweet: '{tweet}'")
        print(f"Sentiment: {sentiment}")
        print("-" * 30)
