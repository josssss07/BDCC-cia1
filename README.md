# BDCC cia 1 project 

## Objective: Perform a comparitive study of python performance and with parallelization 

## Overview and details 

This study aims to evaluate the performance of various Python implementations by measuring processing speed and analyzing the impact of parallelization on algorithm execution. The tasks are divided into two main objectives: comparing Python implementations and investigating the effects of parallelization.

### Languages used for benchmarking: 

- CPython (standard implementation) 
- JPython (python implemented in java)
- PyPy (Alternative python that uses a Just-In-Time compiler)
- Cython (converts python like code to C)
- C (to set a standard benchmark)

### Profiling and parallelization (& cuda if i understand) goes here
Parallel processing can increase the number of tasks done by your program which reduces the overall processing time. These help to handle large scale problems.

In this section we will cover the following topics:

Introduction to parallel processing
Multi Processing Python library for parallel processing
IPython parallel framework
Introduction to parallel processing
For parallelism, it is important to divide the problem into sub-units that do not depend on other sub-units (or less dependent). A problem where the sub-units are totally independent of other sub-units is called embarrassingly parallel.

For example, An element-wise operation on an array. In this case, the operation needs to aware of the particular element it is handling at the moment.

In another scenario, a problem which is divided into sub-units have to share some data to perform operations. These results in the performance issue because of the communication cost.




### References: 

- https://granulate.io/blog/python-performance-testing-quick-tutorial-and-best-practices/
