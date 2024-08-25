import pandas as pd

def load_data(data_set_path: str) -> pd.DataFrame:
    """
    Loading the dataset from a CSV file (NYC_Jobs.csv).
    
    : parameter data_set_path: Path to the CSV file.
    : return: DataFrame containing the loaded data.
    """
    df = pd.read_csv(data_set_path)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleaning the dataset by removing rows with missing values in specific columns, namely, 'Salary Range From', 'Salary Range To', 'Job Category'.
    
    :parameter df: DataFrame to be cleaned.
    :return: The cleaned DataFrame.
    """
    # Displaying NaN values before cleaning
    print("NaNs before cleaning:")
    print(df[['Salary Range From', 'Salary Range To', 'Job Category']].isna().sum())
    
    # Number of rows before cleaning
    df_before = df.shape[0] 
    # Cleaning the NaN's
    df = df.dropna(subset=['Salary Range From', 'Salary Range To', 'Job Category'])
    # Number of rows after cleaning
    df_after = df.shape[0]  
    
    # Display NaN values after cleaning
    print("NaNs after cleaning:")
    print(df[['Salary Range From', 'Salary Range To', 'Job Category']].isna().sum())
    
    print(f"Rows before cleaning: {df_before}")
    print(f"Rows after cleaning: {df_after}")
    return df

def process_data(path_to_csv: str) -> pd.DataFrame:
    """
    Load and clean the dataset.
    
    :param path_to_csv: Path to the CSV file.
    :return: Cleaned DataFrame.
    """
    df = load_data(path_to_csv)
    df = clean_data(df)
    print(df.head(30))  # Print the first 30 rows of the cleaned DataFrame
    return df