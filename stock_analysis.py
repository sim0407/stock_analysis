import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt

# pandas_datareaderのインストール
# !pip install pandas_datareader

# 任天堂の株価を取得（日経平均株価は7974.T）
#TODO Yahoo seems to have changed response format.
def get_nintendo_stock_data(start_date, end_date):
    nintendo_stock = pdr.get_data_yahoo('7974.T', start=start_date, end=end_date)
    return nintendo_stock

# 折れ線グラフを作成
def plot_nintendo_stock_data(nintendo_stock):
    plt.figure(figsize=(12, 6))
    plt.plot(nintendo_stock['Close'], label='Close')
    plt.title('Nintendo Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Price (JPY)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    start_date = '2022-01-01'
    end_date = '2022-12-31'

    nintendo_stock = get_nintendo_stock_data(start_date, end_date)
    plot_nintendo_stock_data(nintendo_stock)