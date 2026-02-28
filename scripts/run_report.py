from obsidianquant.data.market import fetch_ohlcv
from obsidianquant.features.ta import add_ta_features

def main():
    # 拉数据
    df = fetch_ohlcv("NVDA", period="1d", interval="5m")
    # 加技术指标
    df = add_ta_features(df)
    # 转换为美西时间（可选）
    df["Time"] = df["Time"].dt.tz_convert("America/Los_Angeles")
    # 保存 CSV 文件
    df.to_csv("nvda_1d_5m_features.csv", index=False)
    print("CSV saved: nvda_30d_5m_features.csv")
    # 打印一些检查信息
    print("rows:", len(df))
    print("start:", df["Time"].iloc[0])
    print("end:", df["Time"].iloc[-1])
    print(df.tail())

if __name__ == "__main__":
    main()

