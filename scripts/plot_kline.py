from obsidianquant.data.market import fetch_ohlcv
import pandas as pd
import mplfinance as mpf

def to_mpf_df(df: pd.DataFrame) -> pd.DataFrame:
    # df 里 Time 是带时区的 datetime
    out = df.copy()
    out = out.set_index("Time")

    # mplfinance 需要列名严格是: Open High Low Close Volume
    out = out.rename(columns={
        "Open": "Open",
        "High": "High",
        "Low": "Low",
        "Close": "Close",
        "Volume": "Volume",
    })

    # 只保留必要列
    return out[["Open", "High", "Low", "Close", "Volume"]]

def main():
    symbol = "NVDA"
    df = fetch_ohlcv(symbol, period="1d", interval="5m")

    mpf_df = to_mpf_df(df)

    # 画K线 + 成交量 + 20均线（可删）
    mpf.plot(
        mpf_df,
        type="candle",
        volume=True,
        mav=(20,),
        title=f"{symbol} 1d 5m",
        datetime_format="%m-%d %H:%M",
        tight_layout=True,
    )

if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
plt.show()