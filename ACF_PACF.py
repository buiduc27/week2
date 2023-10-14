import pandas as pd #Import thư viện pandas để làm việc với dữ liệu dưới dạng DataFrame.
import numpy as np  # Import thư viện numpy để làm việc với mảng và toán học.
import matplotlib.pyplot as plt # Import thư viện matplotlib để vẽ biểu đồ.
from statsmodels.tsa.stattools import acf, pacf

# Đọc dữ liệu cổ phiếu của APPLE
stock_data = pd.read_csv('/Users/admin/Documents/My Code/PhanTichData/Week2/apple_stock_data.csv')
#Sử dụng pandas để đọc dữ liệu từ tệp tin 'apple_stock_data.csv'. 
# Đây là tệp chứa thông tin giá cổ phiếu của Apple. 
# Đường dẫn tệp này đã được chỉ định trong mã.

# Tính toán ACF và PACF
lag_acf = acf(stock_data['Close'], nlags=20) #sử dụng thư viện statsmodels để tính toán hàm tự tương quan (ACF) cho cột 'Close' của dữ liệu cổ phiếu. 
                                             #Số lags được xác định là 20 (nlags=20), nghĩa là sẽ tính ACF cho 20 lag gần nhất.
lag_pacf = pacf(stock_data['Close'], nlags=20)
# Sử dụng thư viện statsmodels để tính toán hàm tự tương quan một phần (PACF) tương tự như ACF

# Vẽ biểu đồ ACF
plt.subplot(121)
plt.stem(lag_acf)
plt.axhline(y=0, linestyle='--', color='gray')
plt.title('ACF')

# Vẽ biểu đồ PACF
plt.subplot(122)
plt.stem(lag_pacf)
plt.axhline(y=0, linestyle='--', color='gray')
plt.title('PACF')
plt.tight_layout()
plt.show()
