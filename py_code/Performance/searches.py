# importing the required modules
import timeit

# binary search function
def binary_search(mylist, find):
    left, right = 0, len(mylist) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if mylist[mid] == find:
            return True
        elif mylist[mid] < find:  
            left = mid + 1
        else:
            right = mid - 1
    
    return False



# linear search function
def linear_search(mylist, find):
    for x in mylist:
        if x == find:
            return True
    return False


# compute binary search time
def binary_time():
    SETUP_CODE = '''
from __main__ import binary_search
from random import randint'''

    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
binary_search(mylist, find)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # printing minimum exec. time
    print('Binary search time: {}'.format(min(times)))


# compute linear search time
def linear_time():
    SETUP_CODE = '''
from __main__ import linear_search
from random import randint'''

    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
linear_search(mylist, find)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # printing minimum exec. time
    print('Linear search time: {}'.format(min(times)))


if __name__ == "__main__":
    linear_time()
    binary_time()

# This code is modified by Susobhan Akhuli