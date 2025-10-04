import pandas as pd
from fredapi import Fred


def fred_download(api_key='YOUR API_KEY', fred_indicator = 'M2'):

    # Initialize FRED with your API key
    fred = Fred(api_key=api_key)

    if fred_indicator == 'M2':
        fred_indicator = fred_indicator

        # Fetch M2 Money Supply (monthly data, seasonally adjusted)
        m2_data = fred.get_series('M2SL')

        # Convert to DataFrame if needed
        df = pd.DataFrame(m2_data, columns=['M2'])

    df.index.name = 'Date'

    return df