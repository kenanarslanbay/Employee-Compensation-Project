import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Optimized to load data from API by increasing the limit and efficient concatenation	
    """

    base_url = 'https://data.sfgov.org/resource/88g8-5mnd.csv'
    limit = 50000  # Increased limit for fewer, larger requests
    offset = 0
    frames = []  # Use a list to store data frames for later concatenation

    # Define column types outside the loop to avoid repeated definitions
    data_dtypes = {
        'Employee Identifier': pd.Int64Dtype(),
        'Year Type': str,
        'Organization Group Code': pd.Int64Dtype(),
        'Organization Group': str,
        'Department Code': pd.Int64Dtype(),
        'Union Code': pd.Int64Dtype(),
        'Union': str,
        'Job Family Code': pd.Int64Dtype(),
        'Job Family': str,
        'Salaries': float,
        'Overtime': float,
        'Other Salaries': float,
        'Total Salary': float,
        'Retirement': float,
        'Health/Dental': float,
        'Other Benefits': float,
        'Total Benefits': float,
        'Total Compensation': float,
        'Year': str  # Temporarily load as string
    }

    parse_date = ['year']

    while True:
        url = f"{base_url}?$limit={limit}&$offset={offset}"
        response = requests.get(url)
        if response.status_code != 200 or not response.text.strip():
            break
        df_temp = pd.read_csv(io.StringIO(response.text), dtype=data_dtypes, parse_dates=parse_date)
        
        frames.append(df_temp)
        if df_temp.shape[0] < limit:
            break 
        offset += limit
    

    # Concatenate all DataFrame parts into a single DataFrame
    df = pd.concat(frames, ignore_index=True)


    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
