import timeit


def print_cube(num):
    return print(f"Cube = {num * num * num}")


def print_square(num):
    return print(f"Square = {num * num}")


def sort_words(word_list):
    if not isinstance(word_list, list):
        raise ValueError("Input must be a list.")
    print(sorted(word_list, key=str.lower))  # Case-insensitive sorting


def main():
    words = ["Banana", "apple", "Cherry", "date", "Elderberry"]

    print_cube(10)
    print_square(10)
    sort_words(words)
    print("done")


if __name__ == "__main__":
    # Use timeit to measure execution time
    execution_time = timeit.timeit("main()", setup="from __main__ import main", number=1)
    print(f"\nExecution Time: {execution_time:.4f} seconds")
