import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("stock_api")
def get_data():
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=demo' + api_key#"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=Bitcoin&apikey=" + api_key
    response = requests.get(url)
    values = response.json()
    print(values)
    return values
get_data()