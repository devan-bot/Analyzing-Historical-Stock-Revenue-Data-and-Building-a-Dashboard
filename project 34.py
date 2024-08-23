
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch GameStop stock data
gme = yf.Ticker("GME")
gme_data = gme.history(period="1y")

# Reset the index
gme_data_reset = gme_data.reset_index()

# Define the make_graph function if not predefined
def make_graph(df, title):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='green')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plot the GameStop stock data
make_graph(gme_data_reset, 'GameStop Stock Price Over the Last Year')





