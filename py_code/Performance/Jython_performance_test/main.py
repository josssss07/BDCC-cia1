import timeit
import platform
import sys

# Pure recursive Fibonacci function for stress testing
def fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacchi(n - 1) + fibonacchi(n - 2)

# Mean calculation (manual implementation since 'statistics' is unavailable in Jython)
def mean(data):
    return sum(data) / len(data)

# Median calculation
def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2.0
    else:
        return sorted_data[n//2]

# Standard deviation calculation
def stdev(data):
    m = mean(data)
    variance = sum((x - m) ** 2 for x in data) / len(data)
    return variance ** 0.5

# Run a benchmark on the Fibonacci function
def run_benchmark(implementation_name):
    setup_code = "from __main__ import fibonacchi"

    # Test cases chosen to stress the recursive implementation
    test_cases = [20, 25, 35]
    results = {}

    for complexity in test_cases:
        trials = [
            timeit.timeit(
                "fibonacchi({})".format(complexity),
                setup=setup_code,
                number=10  # Run the Fibonacci function 10 times per trial
            ) for _ in range(5)
        ]
        results[complexity] = {
            'mean': mean(trials),
            'median': median(trials),
            'stdev': stdev(trials)
        }

    return results

# Print benchmark results
def print_benchmark(results, implementation_name):
    print("\n" + "=" * 40)
    print("Benchmark for {}".format(implementation_name))
    print("Python version: {}".format(platform.python_version()))
    print("\n" + "=" * 40)

    for complexity, metrics in results.items():
        print("\nComplexity {}:".format(complexity))
        print("  Mean Time:    {:.4f} seconds".format(metrics['mean']))
        print("  Median Time:  {:.4f} seconds".format(metrics['median']))
        print("  Std Deviation: {:.4f} seconds".format(metrics['stdev']))

# Main function
def main():
    implementation_name = platform.python_implementation()
    results = run_benchmark(implementation_name)
    print_benchmark(results, implementation_name)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)  # Increase recursion depth for larger inputs
    main()
