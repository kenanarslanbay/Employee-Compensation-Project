import os
from os import path
import pandas as pd
#import pyarrow as pa
#import pyarrow.parquet as pq
from pandas import DataFrame
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

    


# update the variables below
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/creds.json'
project_id = 'dtc-de-zoomcamp-12345'
bucket_name = 'de-project-data-lake'
object_key = 'employee_data.parquet'
#table_name = 'employee_data'
#root_path = f'{bucket_name}/{table_name}'
format = 'Parguet'


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """

    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Converting year column to datetime format:
    df['year'] = pd.to_datetime(df['year']).dt.year

    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        bucket_name,
        object_key,
        format
    )
