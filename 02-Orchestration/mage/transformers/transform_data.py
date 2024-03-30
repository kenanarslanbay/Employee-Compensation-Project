import pandas as pd
from pandas import DataFrame
from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def execute_combined_transformer_actions(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute multiple transformer actions including normalization, removing duplicates,
    handling missing values, removing unnecessary columns, and excluding rows with zeros
    in specific columns.
    """

    # Cleaning dataframe:
    df = (df.drop_duplicates()
            .dropna()
            .drop(columns=['organization_group_code',
                            'department_code', 'job_family_code', 
                            'job_code', 'union_code'], errors='ignore')
            .query('total_compensation != 0 and total_salary != 0')
            .rename(columns={'employee_identifier':'employee_id'})  # Rename column
            .query("`year_type` == 'Fiscal'"))
    
    
    del df['year_type']

    #adjusting columns positions:

    cols_to_adjust = ['employee_id', 'organization_group', 'department', 'union', 'job_family',
                    'job', 'salaries', 'overtime', 'other_salaries','total_salary', 'retirement',
                    'health_and_dental', 'other_benefits','total_benefits', 'total_compensation','year']

    df = df[cols_to_adjust]

    return df

@test
def test_combined_transformer_action(output, *args) -> None:
    """
    Test for the combined transformer action.
    """
    assert output is not None, 'The output is undefined'
    assert len(output) > 0, 'No data was loaded'
    assert output['total_compensation'].isin([0]).sum() == 0, 'There are zeros in total_compensation columns'