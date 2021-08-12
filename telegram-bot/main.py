# https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={notification_text}
import requests
telegram_endpoint='https://api.telegram.org'
somdgod_stocks_bot='1729364718:AAFncIpc7Tcfve2DuUb3RgwsatXzH9GzmVE'
chat_id='-1001362548332'

parameters={
    'chat_id':chat_id,
    'text':'Test message'
}
bot_endpoint=f"{telegram_endpoint}/bot{somdgod_stocks_bot}/sendMessage"
response=requests.post(url=bot_endpoint,params=parameters)
print(response.json())