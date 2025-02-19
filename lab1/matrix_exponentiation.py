import numpy as np
from benchmark import benchmark_function, plot_benchmark_results


def fibonacci_matrix_exponentiation(n):
    F = np.array([[0, 1], [1, 1]])
    result_vector = np.linalg.matrix_power(F, n) @ np.array([0, 1])
    return result_vector[0]


if __name__ == "__main__":
    n_values = [
        10,
        100,
        500,
        1000,
        2000,
        3000,
        4000,
        5000,
        7500,
        10000,
        15000,
        20000,
        25000,
        30000,
        40000,
        50000,
        60000,
        70000,
        75000,
        80000,
        90000,
        100000,
    ]
    n_values, times, results = benchmark_function(
        fibonacci_matrix_exponentiation, n_values
    )

    plot_benchmark_results(
        n_values,
        times,
        title="Fibonacci Matrix Exponentiation Benchmark",
        xlabel="n (Fibonacci number index)",
    )
