import requests
from twilio.rest import Client
import os

STOCK_NAME = "USDMXN"
COMPANY_NAME = "U.S. Dollar / Mexican Peso"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "KW50O4663Z2RYENC"
NEWS_API_KEY = "c09ac18ce0e44f80b0f82cf85296efd3"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

TWILIO_SID = "AC5f4c0621a4c649ccc1d26a0d1b73cfd1"
TWILIO_TOKEN = '48c021d82bf113e8defb4c3c3ea3d463'


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()['Time Series (Daily)']

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

#If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 0.1:
    #Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": STOCK_NAME,
        "language": "en",
        "sortBy": "relevancy"
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()['articles']

    #Use Python slice operator to create a list that contains the first 3 articles. Hint:
    #  https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.
    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in
                          three_articles]

    #Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            from_='+14797033135',
            body=article,
            to='+525586015653'
        )