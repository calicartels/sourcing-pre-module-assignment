import argparse
import pandas as pd
from data_preprocessing.processor import process_data
from data_preprocessing.visualizer import visualize_salary_distribution

def main():
    # Creating the parser
    parser = argparse.ArgumentParser(description="Processing and displaying dataframe columns from a CSV file")
    
    # Add arguments
    parser.add_argument('csv_path', type=str, help='Path to the CSV file')  # this is to add a positional argument to the cli
    parser.add_argument('--columns', type=str, nargs='+', help='List of columns to display') # this is to add a optional functionality into the cli: to check specific columns
    parser.add_argument('--show', action='store_true', help='Show the first few rows of the DataFrame') # this is to add a optional functionality into the cli: to show the first 30 entries
    parser.add_argument('--visualize', type=str, help='Path to save the salary distribution plot')  # this is to add a optional functionality into the cli: to visualize the salary distribution
    
    # Parse arguments
    args = parser.parse_args()
    
    # Processing the data
    df = process_data(args.csv_path)
    
    # Show selected columns or all columns
    if args.show:
        print("Showing the first 30 rows of the DataFrame:")
        print(df.head(30))
    
    # Displaying the first few rows of the selected columns
    if args.columns:
        print("Selected columns:")
        print(df[args.columns].head(30)) 
    else:
        print("No columns specified. Displaying first 30 rows of the DataFrame:")
        print(df.head(30))
    # Visualizing the Salary Distribution by invoking the visualizer
    if args.visualize:
        visualize_salary_distribution(df, args.visualize)
        print(f"Visualization saved to {args.visualize}")    

if __name__ == "__main__":
    main()