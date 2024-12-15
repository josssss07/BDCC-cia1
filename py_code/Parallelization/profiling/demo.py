import time
import multiprocessing
import cProfile

#is prime: 

def is_prime(num):
    if num < 2: 
        return False
    for i in range (2, int(num ** 0.5) +1):
        if i % 2 == 0:
            return False

    return True

#check all primes in range 
def  check_prime_range(start, end):
    primes = [] 
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    
    return primes

def collect_results(res):
    global all_primes
    all_primes = []

def main():
    global all_primes
    all_primes = []

    # Define the range for prime number calculation
    RANGE_START = 1
    RANGE_END = 1_000_000
    NUM_PROCESSES = multiprocessing.cpu_count()  # Use all available CPUs

    # Split the range into chunks for each process
    step = (RANGE_END - RANGE_START) // NUM_PROCESSES
    ranges = [(RANGE_START + i * step, RANGE_START + (i + 1) * step) for i in range(NUM_PROCESSES)]

    # Use multiprocessing to parallelize the computation
    start_time = time.time()
    with multiprocessing.Pool(processes=NUM_PROCESSES) as pool:
        # Map the ranges to worker processes
        results = pool.starmap(check_prime_range, ranges)

    # Flatten the list of primes
    all_primes = [prime for sublist in results for prime in sublist]
    end_time = time.time()

    print(f"Total primes found: {len(all_primes)}")
    print(f"Time taken with {NUM_PROCESSES} processes: {end_time - start_time:.2f} seconds")

# Function to profile the script
def profile_main():
    cProfile.run('main()')

if __name__ == "__main__":
    profile_main()  # Profile the main function