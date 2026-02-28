import yfinance as yf
import pandas as pd

def fetch_ohlcv(symbol: str, period: str = "30d", interval: str = "10m") -> pd.DataFrame:
    df = yf.download(symbol, period=period, interval=interval, auto_adjust=False, progress=False)
    if df.empty:
        raise RuntimeError(f"No data for {symbol}")
    df = df.rename(columns=str.title)
    df = df.reset_index().rename(columns={"Datetime": "Time", "Date": "Time"})
    return df
