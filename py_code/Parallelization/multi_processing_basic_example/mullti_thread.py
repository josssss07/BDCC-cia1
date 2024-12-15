import multiprocessing as multi
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
    # Word list
    words = ["Banana", "apple", "Cherry", "date", "Elderberry"]

    # Initialize multiprocessing
    p1 = multi.Process(target=print_cube, args=(10,))
    p2 = multi.Process(target=print_square, args=(10,))
    p3 = multi.Process(target=sort_words, args=(words,))

    # Start multiprocessing
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("done")


if __name__ == "__main__":
    # Use timeit to measure execution time
    execution_time = timeit.timeit("main()", setup="from __main__ import main", number=1)
    print(f"\nExecution Time: {execution_time:.4f} seconds")
