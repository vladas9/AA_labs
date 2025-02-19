import time
import matplotlib.pyplot as plt


def benchmark_function(func, n_values):
    func(n_values[0])

    times = []
    results = []
    for n in n_values:
        start_time = time.perf_counter()
        result = func(n)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
        results.append(result)
    return n_values, times, results


def plot_benchmark_results(
    n_values,
    times,
    title="Benchmark Results",
    xlabel="Input Value",
    ylabel="Time (seconds)",
):
    plt.plot(n_values, times, marker="o")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
