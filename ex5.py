import random
import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Implement linear and binary search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 2. Measure performance on sorted vectors
def measure_performance(search_func, data_sizes, iterations=100):
    results = []
    for size in data_sizes:
        arr = list(range(size))  
        target = random.choice(arr)
        time_taken = timeit.timeit(
            stmt=lambda: search_func(arr, target),
            number=iterations
        )
        results.append(time_taken / iterations)
    return results

data_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

# Measure for linear and binary search
linear_results = measure_performance(linear_search, data_sizes)
binary_results = measure_performance(binary_search, data_sizes)

# 3. Interpolate and plot
def plot_results(data_sizes, results, label, fit_func):
    plt.plot(data_sizes, results, 'o', label=f"{label} Data")
    params, _ = curve_fit(fit_func, data_sizes, results)
    plt.plot(data_sizes, fit_func(np.array(data_sizes), *params), '-', label=f"{label} Fit")
    return params

def linear_fit(x, a, b):
    return a * x + b

def logarithmic_fit(x, a, b):
    return a * np.log(x) + b

# plot
plt.figure(figsize=(10, 6))
linear_params = plot_results(data_sizes, linear_results, "Linear Search", linear_fit)
binary_params = plot_results(data_sizes, binary_results, "Binary Search", logarithmic_fit)
plt.xlabel("Data Size")
plt.ylabel("Time (s)")
plt.title("Search Algorithm Performance")
plt.legend()
plt.grid()
plt.show()

# 4. Discussion
# Linear search is O(n), so the time complexity matches a linear function (fit: a*x + b).
# Binary search is O(log n), so the time complexity matches a logarithmic function (fit: a*log(x) + b).
# Parameters:
# Linear search fit parameters: {linear_params}
# Binary search fit parameters: {binary_params}
# The results align with theoretical expectations as linear search grows linearly,
# while binary search grows logarithmically.
