import timeit
import cProfile
import re


def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

profile = cProfile.Profile()
profile.enable()

test_function()
third_function()

profile.create_stats()
profile.print_stats()


# Question 1:
# a profiler collects data to creat a profile, a set of data on how often and how often various parts of the program are executed.

# Question 2:
# While benchmarking just measuress the total time it takes for the program to execute, profiling measures the time of each part of the program. Profiling creates
# relative data, allowing for the comparison of the timings between each part of the program.

# Question 3:
# 

# Question 4
# When running the program, and analyzing the data the profiler gives us, all of the execution time goes to/ comes from the call of the third function.
# Relatively the "third_function" takes alot longer than the other two, as it takes around 10 seconds to execute, while the other two functions take 0 secs to execute.
# This is because in the "third" function, it performs a large amount of calculations, causing it to take a long time to execute.