import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("stock_api")
def get_data():
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=" + stock_api
    response = requests.get(url)
    values = response.json()
    print(values)
    return values
get_data()
