import timeit
import statistics
import platform

def fibonacci(n):
    """Compute fibonacci sequence recursively - a computationally intensive task."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def run_benchmark(implementation_name):
    """Run benchmarks and collect performance metrics."""
    setup_code = "from __main__ import fibonacci"
    
    # Test different complexity levels
    test_cases = [20, 25, 30, 50]
    results = {}
    
    for complexity in test_cases:
        # Run multiple trials to get statistical significance
        trials = [
            timeit.timeit(f"fibonacci({complexity})", 
                setup=setup_code, 
                number=100
            ) for _ in range(5)
        ]
        
        results[complexity] = {
            'mean': statistics.mean(trials),
            'median': statistics.median(trials),
            'stdev': statistics.stdev(trials) if len(trials) > 1 else 0
        }
    
    return results

def print_benchmark_results(results):
    """Pretty print benchmark results."""
    print(f"\n{'='*40}")
    print(f"Benchmark for {platform.python_implementation()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"{'='*40}")
    
    for complexity, metrics in results.items():
        print(f"\nComplexity {complexity}:")
        print(f"  Mean Time:    {metrics['mean']:.4f} seconds")
        print(f"  Median Time:  {metrics['median']:.4f} seconds")
        print(f"  Std Deviation: {metrics['stdev']:.4f} seconds")

def main():
    results = run_benchmark(platform.python_implementation())
    print_benchmark_results(results)

if __name__ == "__main__":
    main()