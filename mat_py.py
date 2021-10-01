import numpy as np
from scipy import stats

array = [6.90,12.60,10.20,5.10,4.30,3.30,4.90,10.20,1.87,10.20,
6.90,6.90,4.90,8.90,7.20,6.90,4.20,9.10,1.84,12.60,
6.90,10.20,4.90,2.20,3.30,8.90,2.20,4.90,8.90,4.90,
9.10,6.90,7.20,8.90,4.90,5.10,6.10,2.20,4.90,11.60,
4.90,6.90,1.30,5.10,1.30,6.00,5.80,6.20,6.90,11.60,
5.10,6.90,3.90,5.90,2.20,6.90,4.40,5.80,7.40,5.10,
5.10,5.10,4.80,3.80,4.90,5.30,6.30,4.90,6.10,7.40,
5.10,6.90,4.30,8.80,8.90,11.60,5.70,5.80,11.60,4.90,
7.10,6.90,4.80,4.90,5.10,11.60,10.20,5.90,7.30,5.10,
12.60,3.30,5.10,8.90,3.60,3.30,5.10,2.20,10.20,2.80]

array.sort()

data = np.array(array)
averageValue = data.mean()
median = np.median(data)
mode = stats.mode(data)
variance = np.var(data)
standardDeviation = np.std(data)
variation = stats.variation(data)
stdRange = data.max()-data.min()
quantiles = [(i/100,np.quantile(data,i/100)) for i in range(0,100,25)]
asymmetry = stats.skew(data)
kurtosis = stats.kurtosis(data)

print(f"Average Value = {averageValue}")
print(f"Median = {median}")
print(f"Mode = {mode}")
print(f"Variance = {variance}")
print(f"Standard Deviation = {standardDeviation}")
print(f"Variation = {variation}")
print(f"Range = {stdRange}")
print(f"Quantiles = {quantiles}")
print(f"Quantiles range = {quantiles[3][1] - quantiles[1][1]}")
print(f"Asymmetry = {asymmetry}")
print(f"Kurtosis = {kurtosis}")