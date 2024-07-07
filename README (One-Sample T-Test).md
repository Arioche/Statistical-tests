# One-Sample T-Test Project

## Project Description

This project involves performing a one-sample t-test on a dataset related to pH values. The goal is to determine whether the mean of the dataset is significantly different from a hypothesized mean.

## Getting Started

### Prerequisites

- Python 3.x
- pandas library
- scipy library

You can install the required libraries using pip:

```bash
python -m pip install pandas scipy


# Import the necessary libraries
import pandas as pd
from scipy.stats import shapiro, ttest_1samp

# Load the data from a CSV file
df = pd.read_csv('C:/Users/admin/Desktop/stat/df.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Perform a Shapiro-Wilk test to check the normality of the 'pH' data
# Note: The Central Limit Theorem (CLT) states that for sample sizes of 30 or more, 
# the distribution of sample means approximates a normal distribution.
result = shapiro(df['pH'])
print("Shapiro-Wilk test result:", result)

# If the p-value is > 0.05, the data is normally distributed.

# Perform a one-sample t-test to determine if the mean of 'pH' is significantly different from the hypothesized mean of 5.6
t_statistic, p_value = ttest_1samp(df['pH'], 5.6)
print(p_value)

# If the p-value is > 0.05, there is no significant difference between the mean of the samples and the population mean.
