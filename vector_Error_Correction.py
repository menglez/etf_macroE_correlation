

from statsmodels.tsa.api import VECM

def vecm(df):


    y, x = df.columns[0], df.columns[1]

    model = VECM(df[[y, x]], k_ar_diff=2, coint_rank=1)
    vecm_res = model.fit()


    print("""If your two series are cointegrated 
    (i.e., they move together in the long run but are individually non-stationary),
    then you should not difference them
     — instead, you should use a Vector Error Correction Model (VECM) 
     rather than Granger causality in difference Series.
    """)
    print(vecm_res.summary())