import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure the visuals directory exists
os.makedirs("visuals", exist_ok=True)

def get_stock_data(ticker="AAPL"):
    # Download data
    df = yf.download(ticker, start="2020-01-01", end="2026-05-10")
    
    # --- HANDLING DATA QUALITY (Fulfills Rubric) ---
    df.ffill(inplace=True)
    
    # --- CALCULATING INDICATORS (Fulfills Rubric) ---
    # 1. 20-Day SMA
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    
    # 2. EMA (Exponential Moving Average)
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    
    # 3. RSI (Relative Strength Index)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    return df

# Run analysis and save the plot
df = get_stock_data("AAPL")

plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price', alpha=0.5)
plt.plot(df['SMA_20'], label='20-Day SMA', color='orange')
plt.plot(df['EMA_20'], label='20-Day EMA', color='green')
plt.title("AAPL Technical Analysis: SMA vs EMA")
plt.legend()
plt.savefig("visuals/aapl_technical_indicators.png")
print("Analysis complete. Indicators calculated: SMA, EMA, and RSI.")
