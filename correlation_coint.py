
from statsmodels.tsa.stattools import coint


def correlation(combined_df):

    correlation = combined_df.iloc[:, 0].corr(combined_df.iloc[:, 1])
    print('correlation', correlation)


    # Assuming your combined_df has two columns
    score, pvalue, _ = coint(combined_df.iloc[:, 0], combined_df.iloc[:, 1])
    print(f"Cointegration p-value: {pvalue} {pvalue < 0.05}")
    if pvalue < 0.05:
        print('We can reject the hypothesis that there is no cointegrating relationship at 5%')
