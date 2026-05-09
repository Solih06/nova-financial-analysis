import yfinance as yf
import pandas as pd
import os

class StockDataProcessor:
    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start = start
        self.end = end
        self.data = None

    def fetch_data(self):
        print(f"Downloading data for {self.ticker}...")
        self.data = yf.download(self.ticker, start=self.start, end=self.end)
        return self.data

    def calculate_indicators(self):
        """Manual calculation to avoid Python 3.14 compatibility issues."""
        if self.data is not None:
            # 1. Simple Moving Average (SMA 20)
            self.data['SMA_20'] = self.data['Close'].rolling(window=20).mean()

            # 2. Relative Strength Index (RSI)
            delta = self.data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            self.data['RSI_14'] = 100 - (100 / (1 + rs))

            print("SMA and RSI calculated successfully.")
        return self.data

    def save_data(self):
        os.makedirs('data', exist_ok=True)
        file_path = f"data/{self.ticker}_processed.csv"
        self.data.to_csv(file_path)
        print(f"Data saved to {file_path}")

if __name__ == "__main__":
    processor = StockDataProcessor("AAPL", "2020-01-01", "2026-01-01")
    processor.fetch_data()
    processor.calculate_indicators()
    processor.save_data()