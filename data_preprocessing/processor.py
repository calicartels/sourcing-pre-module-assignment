import pandas as pd

def load_data(data_set_path: str) -> pd.DataFrame:
    """
    Load the dataset(NYC jobs dataset) from the csv file which has been packaged in the repo
    : parameter data_set_path: path to the csv file and it is input as a string
    : return : the processed information is returned in the form of a dataframe.
    """

def clean_data(df : pd.DataFrame) -> pd.DataFrame:
    """
    Cleaning the dataset.
    : parameter df: input, it is the original DataFrame which has been read in the load_data.
    : return : the cleaned dataset in a DataFrame format.
    
    """

    ## Here the nan values in the rows from columns : "Salary Range From', 'Salary Range To', 'Job Category' are removed.
    df = df.dropna(subset=['Salary Range From', 'Salary Range To', 'Job Category'])
    return df

def process_data(path_to_csv: str) -> pd.DataFrame:
    """
    Calling the functions to load and clean the dataset.

    :paramter file_path: Path to the CSV file.
    :return: Cleaned DataFrame.
    """
    df = load_data("NYC_Jobs.csv")
    df = clean_data(df)
    return df