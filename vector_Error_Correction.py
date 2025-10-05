

from statsmodels.tsa.api import VECM

#def vecm(df):
def vecm(df, k_ar_diff=2, coint_rank=1):
    """
        Fit and analyze a VECM between two series.

        Parameters:
            df : pd.DataFrame
                Must contain exactly two columns, e.g. ['SPY', 'GDP']
            k_ar_diff : int
                Number of lag differences to include.
            coint_rank : int
                Cointegration rank.
    """


    y, x = df.columns[0], df.columns[1]

    # Fit model
    model = VECM(df[[y, x]], k_ar_diff=k_ar_diff, coint_rank=coint_rank)
    vecm_res = model.fit()



    print("""If your two series are cointegrated 
    (i.e., they move together in the long run but are individually non-stationary),
    then you should not difference them
     — instead, you should use a Vector Error Correction Model (VECM) 
     rather than Granger causality in difference Series.
    """)

    print("\n=================== SUMMARY ===================")
    print(vecm_res.summary())

    print("\n================= INTERPRETATION =================")

    # 1. Cointegration relationship (β vector)
    beta = vecm_res.beta[:, 0]
    print(f"\nCointegration relation (normalized): {y} + ({beta[1]:.4f}) * {x} = 0")
    if beta[1] > 0:
        print(f"→ {y} and {x} move in the same long-term direction.")
    else:
        print(f"→ {y} and {x} move in opposite long-term directions.")

    # 2. Adjustment coefficients (α)
    alpha = vecm_res.alpha[:, 0]
    print("\nAdjustment (Error Correction) coefficients:")
    print(f"  {y}: {alpha[0]:.4f}")
    print(f"  {x}: {alpha[1]:.4f}")
    if abs(alpha[0]) > abs(alpha[1]):
        print(f"→ {y} adjusts faster to restore equilibrium.")
    elif abs(alpha[1]) > abs(alpha[0]):
        print(f"→ {x} adjusts faster to restore equilibrium.")
    else:
        print(f"→ Both series adjust at similar rates.")

    # 3. Short-run dynamics (lagged differenced terms)
    print("\nShort-run dynamics significance (p-values):")
    sr_pvalues = vecm_res.pvalues
    print(sr_pvalues)
    sig_params = sr_pvalues[(sr_pvalues < 0.05)].index.tolist()
    if sig_params:
        print(f"\nSignificant short-run effects (p<0.05): {sig_params}")
    else:
        print("\nNo significant short-run lag effects at 5% level.")

    # 4. Stability check
    eigs = vecm_res.roots
    stable = np.all(np.abs(eigs) < 1)
    print("\nStability of system:")
    print(f"  Eigenvalues: {np.round(eigs, 3)}")
    print(f"  → Model is {'stable' if stable else 'unstable'} (all |λ|<1).")

    # 5. Return object for further IRF/FEVD/forecasting
    #return vecm_res