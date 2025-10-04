import datetime
import yfinance as yf
import pandas as pd


end_date = datetime.date.today()
# start_date = end_date.replace(year=end_date.year - 10)

start_date = datetime.datetime(2000, 1, 1)
######start_date = datetime(2020, 6, 6)



def etf_download(etf='SPY'):

    list_etf_ticker = [etf]


    # Download data for the ETFs and get only 'Adj Close'
    try:
        # Fetch the data for all ETFs
        df_data = yf.download(list_etf_ticker, start=start_date, end=end_date, auto_adjust=False)['Adj Close']

        # removing ceros from the index date
        df_data.index = pd.to_datetime(df_data.index, utc=True)
        df_data.index = df_data.index.date

        return df_data

    except Exception as e:
        print(f"An error occurred: {e}")


    return ''