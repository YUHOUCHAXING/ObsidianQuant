from obsidianquant.data.market import fetch_ohlcv
from obsidianquant.features.ta import add_ta_features

def main():
    df = fetch_ohlcv("NVDA")
    df = add_ta_features(df)
    print(df.tail())

if __name__ == "__main__":
    main()
