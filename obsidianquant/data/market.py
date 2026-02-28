import yfinance as yf
import pandas as pd

def fetch_ohlcv(symbol: str,
                period: str = "1d",
                interval: str = "5m") -> pd.DataFrame:

    print("fetch_ohlcv called with:", symbol, period, interval)

    df = yf.download(
        symbol,
        period=period,
        interval=interval,
        auto_adjust=False,
        progress=False
    )

    if df is None or df.empty:
        raise RuntimeError(f"No data for {symbol}")

    # 如果列是 MultiIndex，拍平
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] for c in df.columns]

    # 统一列名
    df = df.rename(columns=str.title)

    # 重置索引
    df = df.reset_index().rename(columns={"Datetime": "Time", "Date": "Time"})

    return df

