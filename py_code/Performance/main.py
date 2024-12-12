import timeit
import statistics
import platform
import sys


'''Pure recursive Fibonacci function for stress testing'''
def fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacchi(n - 1) + fibonacchi(n - 2)


'''Run a benchmark on the Fibonacci function'''
def run_benchmark(implementation_name):
    setup_code = "from __main__ import fibonacchi"

    # Test cases chosen to stress the recursive implementation
    test_cases = [20, 25, 30]
    results = {}

    for complexity in test_cases:
        trials = [
            timeit.timeit(
                f"fibonacchi({complexity})",
                setup=setup_code,
                number=1  # Only one run per trial due to recursion's high cost
            ) for _ in range(5)
        ]
        results[complexity] = {
            'mean': statistics.mean(trials),
            'median': statistics.median(trials),
            'stdev': statistics.stdev(trials)
        }

    return results


'''Print benchmark results'''
def print_benchmark(results, implementation_name):
    print(f"\n{'=' * 40}")
    print(f"Benchmark for {implementation_name}")
    print(f"Python version: {platform.python_version()}")
    print(f"\n{'=' * 40}")

    for complexity, metrics in results.items():
        print(f"\nComplexity {complexity}:")
        print(f"  Mean Time:    {metrics['mean']:.4f} seconds")
        print(f"  Median Time:  {metrics['median']:.4f} seconds")
        print(f"  Std Deviation: {metrics['stdev']:.4f} seconds")


# Main function
def main():
    implementation_name = platform.python_implementation()
    results = run_benchmark(implementation_name)
    print_benchmark(results, implementation_name)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)  # Increase recursion depth for larger inputs
    main()
