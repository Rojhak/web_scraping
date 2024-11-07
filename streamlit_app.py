import pandas as pd
import streamlit as st

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add your service account credentials
creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/fehmikatar/Desktop/Code_Berlin/web_scrabing/web_scraping_git/service_account.json', scope)

# Authorize the client
client = gspread.authorize(creds)
sheet = client.open("stock_price").sheet1
data = sheet.get_all_values()

df = pd.DataFrame(data[1:], columns=data[0])  # Use the first row as header

# Convert relevant columns to numeric types and handle dates
df['date'] = pd.to_datetime(df['date'])  # Ensure 'dates' is in datetime format
df['open'] = pd.to_numeric(df['open'], errors='coerce')
df['high'] = pd.to_numeric(df['high'], errors='coerce')
df['low'] = pd.to_numeric(df['low'], errors='coerce')
df['close'] = pd.to_numeric(df['close'], errors='coerce')
df['volume'] = pd.to_numeric(df['volume'], errors='coerce')

# Set the date column as the index
df.set_index('date', inplace=True)

# Create a line chart
st.title('Stock Data Line Chart')

# Create line charts for open, high, low, close prices
st.subheader('Stock Prices')
st.line_chart(df[['open', 'high', 'low', 'close']])

# Optionally, create a line chart for volume
st.subheader('Trading Volume')
st.line_chart(df['volume'])