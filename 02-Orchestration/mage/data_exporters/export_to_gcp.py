import os
from os import path
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pandas import DataFrame
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

    
# config_path = path.join(get_repo_path(), 'io_config.yaml')
# config_profile = 'default'

# update the variables below
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/creds.json'
project_id = 'dtc-de-zoomcamp-12345'
bucket_name = 'de-project-data-lake'
object_key = 'employee_data.parquet'
table_name = 'employee_data'
root_path = f'{bucket_name}/{table_name}'


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """

    # # Ensure 'year' column is a datetime type to extract the year component
    # if df['year'].dtype == 'datetime64[ns]':
    #     df['year'] = df['year'].dt.year
    # elif df['year'].dtype == 'object' or df['year'].dtype == 'string_':
    #     # Attempt to convert to datetime first if stored as string/object
    df['year'] = pd.to_datetime(df['year']).dt.year

    table = pa.Table.from_pandas(df)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        #partition_cols=['year'],
        filesystem=gcs
    )
