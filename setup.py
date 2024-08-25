from setuptools import setup, find_packages

setup(
    name="nyc_jobs_analysis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pandas", "matplotlib","pytest", "argparse"],
    entry_points={
        "console_scripts": [
            "nyc_jobs_analysis=nyc_jobs_analysis.cli:main",
        ],
    },
    test_suite="tests",
)
