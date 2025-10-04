
from statsmodels.tsa.stattools import grangercausalitytests

def causality(combined_df, max_lag = 5):

    # Clean and prepare your data
    df = combined_df.dropna()

    y, x = df.columns[0], df.columns[1]
    data = df[[y, x]]


    # Set max lag
    max_lag = max_lag

    # Run Granger causality tests
    results = grangercausalitytests(data, maxlag=max_lag)
    causality_results = {}

    # Print formal summary of p-values
    #print(f"\nGranger Causality Test: Does '{series2_name}' help predict '{series1_name}'?\n")
    print(f"\nGranger Causality Test: Does '{x}' help predict '{y}'?\n")

    for lag in range(1, max_lag + 1):
        ssr_f_p    = results[lag][0]['ssr_ftest'][1]
        ssr_chi2_p = results[lag][0]['ssr_chi2test'][1]
        lr_p       = results[lag][0]['lrtest'][1]

        causality_results[lag] = {
            'f_p': ssr_f_p,
            'chi2_p': ssr_chi2_p,
            'lr_p': lr_p
        }

        print('')
        print('------------Granger Causality--------------')
        print(f"Lag {lag}:")
        print(f"  SSR F-test p-value       = {ssr_f_p:.4f}")
        print(f"  Chi-squared p-value      = {ssr_chi2_p:.4f}")
        print(f"  Likelihood Ratio p-value = {lr_p:.4f}")

        if ssr_f_p < 0.05 or ssr_chi2_p < 0.05 or lr_p < 0.05:
            print(f"✅ Evidence: {x} Granger-causes {y} at lag {lag}.")
        else:
            print(f"❌ No significant causality at lag {lag}.")
        print()

