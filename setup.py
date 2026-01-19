from setuptools import setup, find_packages

setup(
    name="contract-prediction",
    version="0.1.0",
    author="Geovanny Rodriguez",
    description="Machine Learning project to predict contract outcomes",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn"
    ],
)
