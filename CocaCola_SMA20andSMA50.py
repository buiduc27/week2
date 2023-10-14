import yfinance as yf
import pandas as pd
import mplfinance as mpf

symbol = 'KO'
start_date = '2022-10-14'
end_date = '2023-10-14'

data = yf.download(symbol, start=start_date, end=end_date)
data.to_csv("coca_data.csv")

sma20 = data['Close'].rolling(window=20).mean()
sma50 = data['Close'].rolling(window=50).mean()

sma_data = pd.DataFrame({'SMA20': sma20, 'SMA50': sma50})

combined_data = pd.concat([data, sma_data], axis=1)

mpf.plot(combined_data, type="candle", style="yahoo", title="Biểu đồ nến của Coca và Đường SMA20, SMA50", ylabel="Giá", addplot=[
    mpf.make_addplot(sma20, color='red', secondary_y=False),
    mpf.make_addplot(sma50, color='blue', secondary_y=False)
])
