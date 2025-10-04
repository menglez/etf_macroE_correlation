import pandas as pd
from fredapi import Fred


def fred_download(api_key='YOUR API_KEY', fred_indicator = 'M2SL'):

    # Initialize FRED with your API key
    fred = Fred(api_key=api_key)

    fred_indicator = fred_indicator

    fred_indicator = fred_indicator

    # Fetch M2 Money Supply (monthly data, seasonally adjusted)
    data = fred.get_series(fred_indicator)

    # Convert to DataFrame if needed
    df = pd.DataFrame(data, columns=[fred_indicator])

    df.index.name = 'Date'

    return df