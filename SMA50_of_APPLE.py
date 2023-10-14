import yfinance as yf
import pandas as pd
import mplfinance as mpf

symbol = 'AAPL'  # Mã chứng khoán của Apple
start_date = '2022-10-01'
end_date = '2023-10-01'

# Tải dữ liệu lịch sử giá cổ phiếu Apple từ Yahoo Finance và lưu vào file CSV
data = yf.download(symbol, start=start_date, end=end_date)
data.to_csv('apple_stock_data.csv')

# Tính toán đường SMA20
sma20 = data['Close'].rolling(window=20).mean()
sma50 = data['Close'].rolling(window = 50).mean()

# Tạo DataFrame mới chứa dữ liệu SMA20
sma_data = pd.DataFrame({'SMA20': sma20, 'SMA50': sma50})

# Kết hợp dữ liệu giá và dữ liệu SMA20
combined_data = pd.concat([data, sma_data], axis=1)

# Đọc dữ liệu từ file CSV và thiết lập index là ngày
data = pd.read_csv("apple_stock_data.csv", index_col=0, parse_dates=True)

# Tạo biểu đồ nến sử dụng mplfinance
mpf.plot(combined_data, type="candle", style="yahoo", title="Biểu đồ giá Apple", ylabel="Giá", addplot=[
    mpf.make_addplot(sma20, color='red', secondary_y=False),
    mpf.make_addplot(sma50, color='blue', secondary_y=False)
])
