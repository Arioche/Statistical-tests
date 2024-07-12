import pandas as pd
from scipy.stats import wilcoxon
#or import scipy.stats as stats,
#stats.wilcoxon(first_data, Second_data)

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