from benchmark import benchmark_function, plot_benchmark_results


def fibonacci_iterative_memo(n):
    if n <= 1:
        return n

    fib_numbers = [0] * (n + 1)
    fib_numbers[1] = 1

    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]

    return fib_numbers[n]


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
    n_values, times, results = benchmark_function(fibonacci_iterative_memo, n_values)

    plot_benchmark_results(
        n_values,
        times,
        title="Fibonacci Iterative Memo Benchmark",
        xlabel="n (Fibonacci number index)",
    )
