import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPH_URL = "https://www.alphavantage.co/query"
ALPH_API_KEY = "enter api key"
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "enter api key"


# Twilio Credentials
account_sid = "enter your account sid"
auth_token = "enter your tokin"
client = Client(account_sid, auth_token)

# Fetch stock data from Alpha Vantage
alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPH_API_KEY
}

response = requests.get(url=ALPH_URL, params=alpha_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

# Get the two most recent trading days
data_list = list(stock_data.keys())
recent_date = data_list[0]
previous_date = data_list[1]

recent_price = float(stock_data[recent_date]["4. close"])
previous_price = float(stock_data[previous_date]["4. close"])

# Calculate percentage change
percent_change = ((recent_price - previous_price) / previous_price) * 100
print(f"Percentage change: {percent_change}%")

# Check if the percentage change is significant
if abs(percent_change) >= 5:
    # Fetch news if significant change
    news_params = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
        "language": "en"
    }
    news_response = requests.get(url=NEWS_URL, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json().get("articles", [])[:3]

    # Determine direction icon
    if percent_change > 0:
        up_down_icon = "🔺"
    else:
        up_down_icon = "🔻"
    formatted_percent = f"{abs(percent_change):.2f}%"
    # Send top 3 news articles via SMS
    for article in articles:
        title = article.get("title", "No title available")
        description = article.get("description", "No description available")

        message_body = (
            f"{STOCK}: {up_down_icon}{formatted_percent}\n"
            f"Headline: {title}\n"
            f"Brief: {description}"
        )

        message = client.messages.create(
            body=message_body,
            from_="",    # Your Twilio phone number
            to=""    # Recipient's phone number
        )

