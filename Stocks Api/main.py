import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY="09NUEAPD8JER1VIG"
NEWS_API_KEY='128acd9ba29b44698fca0a844c57a326'

telegram_endpoint='https://api.telegram.org'
somdgod_stocks_bot='1729364718:AAFncIpc7Tcfve2DuUb3RgwsatXzH9GzmVE'
chat_id='-1001362548332'

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
# print(data)
data_list = [value for (key, value) in data.items()]
# print(data_list)
yesterday_data = data_list[0]
yesterday_data_closeprice = yesterday_data['4. close']
print("Yesterday closing=", yesterday_data_closeprice)

# Get the day before yesterday's closing stock price
daybfore_yesterday_data = data_list[1]
daybefore_yesterday_data_closeprice = yesterday_data['4. close']
print("day before Yesterday closing=", daybefore_yesterday_data_closeprice)
# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_data_closeprice) - float(daybefore_yesterday_data_closeprice))
print("difference=", difference)
# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_data_closeprice)) * 100
print("Difference percentage=", diff_percent)
news_headers = {
    'X-Api-Key': NEWS_API_KEY,
}
news_params = {
    'qInTitle': COMPANY_NAME
}
news_response = requests.get(url=NEWS_ENDPOINT, headers=news_headers, params=news_params)
articles = news_response.json()['articles']
# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
formatted_article = [f"Headlines: {article['title']}. \n Brief:{article['description']}\nURL:{article['url']}" for
                     article in articles[:5]]
print(formatted_article)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.

formatted_stock_prices = f"Yesterday closing={yesterday_data_closeprice} \n day before Yesterday closing={daybefore_yesterday_data_closeprice}\n difference={difference}\n difference percentage= {diff_percent}"
stock_prices = {
    'chat_id': chat_id,
    'text': formatted_stock_prices
}
bot_endpoint = f"{telegram_endpoint}/bot{somdgod_stocks_bot}/sendMessage"
response2 = requests.post(url=bot_endpoint, params=stock_prices)
print(response2.json())
for article in articles[:5]:
    stock_articles = {
        'chat_id': chat_id,
        'text': formatted_article,
    }
    response1 = requests.post(url=bot_endpoint, params=stock_articles)
    print(response1.json())



