import pandas as pd
import matplotlib.pyplot as plt

def visualize_salary_distribution(df: pd.DataFrame, output_path: str):
    """
    Visualize the salary distribution and saving the plot.

    :parameter df: The DataFrame containing the dataset.
    :parameter output_path: Path to save the plot image.
    """
    plt.figure(figsize=(10, 6))
    df['Salary Range From'].plot(kind='hist', bins=50, alpha=0.7, label='Salary Range From')
    df['Salary Range To'].plot(kind='hist', bins=50, alpha=0.7, label='Salary Range To')
    plt.title('Salary Distribution')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(output_path)
    plt.close()