import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("visuals", exist_ok=True)
df = yf.download("AAPL", start="2020-01-01", end="2026-05-10")
df.ffill(inplace=True)
df["SMA_20"] = df["Close"].rolling(window=20).mean()

plt.figure(figsize=(12,6))
plt.plot(df["Close"], label="Price")
plt.plot(df["SMA_20"], label="20-Day SMA")
plt.title("AAPL Technical Indicators - SMA 20")
plt.legend()
plt.savefig("visuals/aapl_technical_indicators.png")
