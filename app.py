import pandas as pd
import download_fred      #FRED function
import download_etf
import causalty_test
import correlation_coint
import ploting_all
#import etf_resample



api_key = input('ENTER FRED API_KEY and press ENTER >> ')
etf_input = input('ENTER ETF and press ENTER >> ')

print('FRED INDICATORs ', 'M2SL', 'FEDFUNDS', 'GS10', 'MORTGAGE30US')
fred_ind_inp = input("ENTER FRED INDICATOR and press ENTER >> ")



etf = etf_input.upper()
fred_indicator=fred_ind_inp


etf_df = download_etf.etf_download(etf)
fred_df = download_fred.fred_download(api_key=api_key, fred_indicator=fred_indicator)
#mon_df = etf_resample.monthly_resample(etf_df)




#combined_df = pd.concat([ mon_df, fred_df], axis=1).dropna()
combined_df = pd.concat([ etf_df, fred_df], axis=1).dropna()
print(combined_df)

correlation_coint.correlation(combined_df)
causalty_test.causality(combined_df)


print('\n===================================\n')


cb_diff_df   = combined_df.copy()
cb_diff_df['diff_etf']   = cb_diff_df[etf].diff()
cb_diff_df['diff_ind']   = cb_diff_df[fred_indicator].diff()
cb_diff_df = cb_diff_df.drop(columns=[etf])
cb_diff_df = cb_diff_df.drop(columns=[fred_indicator])
cb_diff_df = cb_diff_df.dropna()




correlation_coint.correlation(cb_diff_df)
causalty_test.causality(cb_diff_df)


print('\n===================================\n')
ploting_all.plot_all(combined_df, cb_diff_df, increase_etf=True)