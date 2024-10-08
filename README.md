# Sourcing for Data Analytics

Premodule Assignment - AIPI 510 

## Problem Statement

Create a Python script that does some specific task (i.e. process a csv file in some way), write unit tests for it, and package it into a command line tool.

## Objective 

The objective I have chosen is to modify the dataset by removing the NaN or Null Values from a subset of the Dataset.
Here, columns "Salary Range To", "Salary Range From", and "Job Category" are modified to remove the NaNs.

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
└── venv/  
```
## About the Dataset

- The original dataset can be found here: [New York City Job Dataset](https://www.kaggle.com/datasets/anoopjohny/new-york-city-job-dataset)
- A subset of this Dataset has been considered for the project by considering only the first 15 columns (Which has been packaged in the project)

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/calicartels/sourcing-pre-module-assignment.git
```

or 

Download the Zip file locally.

### 2. Navigate to the project directory
```bash
cd sourcing-pre-module-assignment
```

### 3. Install the required packages
```bash
pip install -e .
```

### 4. Set up the virtual environment (if needed)

```bash
python3 -m venv venv
```
or 

```bash
python -m venv venv
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

### Installing reqy=uirements
```bash
pip install -r requirements.txt
```

### To Show the output of the dataset before and after the processing is done
```bash
python -m data_preprocessing.cli NYC_Jobs.csv --show
```

### Visualize the salary distribution

The image is saved as a `.png` file in the source directory

```bash
python -m data_preprocessing.cli NYC_Jobs.csv --visualize salary_distribution.png
```

### Display specific columns
Command :

```bash
python -m data_preprocessing.cli NYC_Jobs.csv --columns "NAME OF THE COLUMN_1" "NAME OF THE COLUMN_1"
```
Example :

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
- Better Pull Requests on Github or better use of Git in general
- Argparse for CLI commands

## License

This project is licensed under the MIT License.
