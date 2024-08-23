import argparse
from .processor import process_data
from .visualizer import visualize_salary_distribution

def main():
    parser = argparse.ArgumentParser(description="Process and visualize NYC Jobs data.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_plot", help="Path to save the salary distribution plot")
    
    args = parser.parse_args()

    df = process_data(args.input_file)
    visualize_salary_distribution(df, args.output_plot)
    print(f"Data processed and plot saved to {args.output_plot}")

if __name__ == "__main__":
    main()