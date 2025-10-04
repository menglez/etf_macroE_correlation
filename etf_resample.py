import pandas as pd

def monthly_resample(etf_df):

    df_tmp1 = etf_df.copy()

    # Step 1: Ensure datetime index
    df_tmp1.index = pd.to_datetime(df_tmp1.index)

    # Step 2: Create a monthly index with first day of each month
    monthly_index = pd.date_range(start=df_tmp1.index.min(), end=df_tmp1.index.max(), freq='MS')

    # Step 3: Reindex your data to this monthly index
    mon_df = df_tmp1[df_tmp1.columns[0]].reindex(monthly_index)

    # Step 4: Fill missing values using interpolation or forward-fill
    mon_df = mon_df.interpolate(method='time')  # or .ffill()

    return mon_df