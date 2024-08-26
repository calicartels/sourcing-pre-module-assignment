import pytest
import pandas as pd
from data_preprocessing.processor import clean_data

@pytest.fixture
def real_data():
    """
   Loading my Dataset
    """
    return pd.read_csv('NYC_Jobs.csv')

def test_load_data(real_data):
    """
    testing to see if the data has been loaded as a dataframe
    parameter real_data: loaded dataset simulation
    """
    assert isinstance(real_data,pd.DataFrame)

def test_clean_data(real_data):

    """
    Testing the clean data function to see if the processed dataframe has been removed of the NaN's, if the columns have been presented.
    parameter real_data: loaded dataset simulation.

    """
    # Clean the dataset
    df_cleaned = clean_data(real_data)
    
    # Assert that the cleaned DataFrame has fewer rows than the original
    assert df_cleaned.shape[0] < real_data.shape[0]
    
    # Assert that no rows have missing values in the specified columns
    assert df_cleaned[['Salary Range From', 'Salary Range To', 'Job Category']].isna().sum().sum() == 0

    # Ignore extra columns and focus only on expected ones
    expected_columns = ['Job ID', 'Agency', 'Posting Type', 'Salary Range From', 'Salary Range To', 'Job Category']
    df_expected_cleaned = real_data[expected_columns].dropna(subset=expected_columns)
    pd.testing.assert_frame_equal(df_cleaned[expected_columns], df_expected_cleaned)
