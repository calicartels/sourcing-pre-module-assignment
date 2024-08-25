# Sourcing for Data Analytics

Premodule Assignment - AIPI 510 

## Problem Statement

Create a Python script that does some specific task (i.e. process a csv file in some way), write unit tests for it, and package it into a command line tool.

## Project Structure

```plaintext
sourcing_for_data_analytics/
├── data_preprocessing/
│   ├── __init__.py
│   ├── processor.py
│   └── cli.py
├── test/
│   └── test_processor.py
├── README.md
├── requirements.txt
├── setup.py
└── venv/  # virtual environment directory 
```
## About the Dataset

- The original dataset can be found here: [New York City Job Dataset](https://www.kaggle.com/datasets/anoopjohny/new-york-city-job-dataset)
- A subset of this Dataset has been considered for the project by considering only the first 15 columns.

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/calicartels/sourcing-pre-module-assignment.git
```

or 

Download the Zip file locally.

### 2. Navigate to the project directory
```bash
cd Sourcing_for_Data_Analytics
```

### 3. Install the required packages
```bash
pip install -e .
```

### 4. Set up the virtual environment (if needed)

```bash
python3 -m venv venv
```
#### Activate the environment:
#### Windows:

```bash
.\venv\Scripts\activate
```
#### Mac:

```bash
source venv/bin/activate
```


## Usage

### To Show the output of the dataset before and after the processing is done
```bash
python -m data_preprocessing.cli NYC_Jobs.csv --show
```

### Visualize the salary distribution
```bash
python -m data_preprocessing.cli NYC_Jobs.csv --visualize salary_distribution.png
```

### Display specific columns
```bash
python -m data_preprocessing.cli NYC_Jobs.csv --columns "Salary Range To"
```

## Testing

### Run tests
To run the tests and verify that the data processing functions work correctly, use the following command:

```bash
pytest test/test_processor.py -v
```

## References

- [Testing with Pytest for Data Science - Ravin Kumar](https://www.youtube.com/watch?v=dY1nNtDTruE)
- [pytest Tutorial: How to write tests in Python | Data Science](https://www.youtube.com/watch?v=bhjaQssIXiw)
- [Python Essentials for MLOps](https://www.coursera.org/learn/python-mlops-duke/home/welcome)
- [pytest](https://docs.pytest.org/en/stable/explanation/fixtures.html)
- [Premodule Resources](https://canvas.duke.edu/courses/40118/files/1500172?module_item_id=272098)
- [How To Pull Request in 3 Minutes](https://www.youtube.com/watch?v=jRLGobWwA3Y)
- ChatGPT for finetuning my README.md
  
## Stuff That I'm Still Learning and would want to implement in the future xD

- Generating PyTests for Matplotlib functions.
- Better Pull Requests on Github
- Argparse for CLI commands
- 
## License

This project is licensed under the MIT License.
