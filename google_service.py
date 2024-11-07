from main import get_data
import gspread
import pandas as pd

def save_data():
    # fetch data from api
    data = get_data()

    # transform data into dataframe with two columns: date, price (close)
    dates = []
    open = []
    high = []
    low = []
    close = []
    volume = []
    for date in data["Time Series (Digital Currency Daily)"]:
        dates.append(date)
        open.append(data['Time Series (Digital Currency Daily)'][date]['1. open'])
        high.append(data['Time Series (Digital Currency Daily)'][date]['2. high'])
        low.append(data['Time Series (Digital Currency Daily)'][date]['3. low'])
        close.append(data['Time Series (Digital Currency Daily)'][date]['4. close'])
        volume.append(data['Time Series (Digital Currency Daily)'][date]['5. volume'])
    df = pd.DataFrame({ "date": dates, "high":high, "open": open, "low":low, "close":close, "volume":volume })

    # connect to Google worksheet
    gc = gspread.service_account(filename="./service_account.json")
    worksheet = gc.open("stock_price").sheet1

    # update the Google worksheet
    worksheet.update(values=[df.columns.values.tolist()] + df.values.tolist(), range_name='my_range')
save_data()