import time
import matplotlib.pyplot as plt
from numpy import random

def generate_random_array(n, min_val=0, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(n)]

def benchmark_function(func, n_values):
    func(generate_random_array(n_values[0])) 

    times = []
    results = []
    for n in n_values:
        arr = generate_random_array(n) 
        start_time = time.perf_counter()
        result = func(arr)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
        results.append(result)
    return n_values, times, results

def plot_benchmark_results(
    n_values,
    times,
    title="Benchmark Results",
    xlabel="Input Size (n)",
    ylabel="Time (seconds)",
):
    plt.plot(n_values, times, marker="o", linestyle="-")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
