import numpy as np
from benchmark import benchmark_function, plot_benchmark_results
from decimal import Decimal, getcontext


def fibonacci_binet_decimal(n):
    getcontext().prec = 20
    phi = (1 + Decimal(5).sqrt()) / 2
    psi = (1 - Decimal(5).sqrt()) / 2
    return int((phi**n - psi**n) / Decimal(5).sqrt())


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
    ]
    n_values, times, results = benchmark_function(fibonacci_binet_decimal, n_values)

    plot_benchmark_results(
        n_values,
        times,
        title="Fibonacci Binet Benchmark",
        xlabel="n (Fibonacci number index)",
    )
