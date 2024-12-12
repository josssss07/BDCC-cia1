# fibonacci.pyx

# Declare the function and variable types for Cython optimization
def fibonacci(int n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
