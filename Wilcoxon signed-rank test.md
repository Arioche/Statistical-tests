The Wilcoxon signed-rank test is a non-parametric test, which means it does not assume that the data follow a specific distribution, such as the normal distribution. 
This makes it suitable for data that do not meet the assumptions of parametric tests, such as data that are not normally distributed.

In the one-sample Wilcoxon signed-rank test, the median of the data is compared to a hypothetical median.

You can use the sample code below that I have used for Non-Normal distributed pH results.

Python

import pandas as pd
from scipy.stats import wilcoxon

# Load the data
df = pd.read_csv('df.csv')

# Define the hypothetical median value
hypothetical_median = 5.6

# Subtract the hypothetical median from the sample
data = df['NonNormalpH'] - hypothetical_median

# Perform the Wilcoxon signed-rank test
w, p = wilcoxon(data)

print('The Wilcoxon signed-rank test statistic value is:', w)
print('The p-value is:', p)
