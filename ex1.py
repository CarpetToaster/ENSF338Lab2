import timeit
import matplotlib.pyplot as plt
'''
i) this is the fibonacci sequence

ii) this isn't really "divide" and conquer, as it actually causes some already solved instances to get solved several times

iii) O(n^2) since each call reduces the overall n by 1 but multiples it again by 2
'''

def fibMemo(n, doneDict = {}):
    if n == 0 or n == 1:
        doneDict[n] = n
        return doneDict[n]
    elif n in doneDict:
        return doneDict[n]   
    else:
        doneDict[n] = fibMemo(n-1, doneDict) + fibMemo(n-2, doneDict)
    return doneDict[n]       
        

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
'''
v) O(n) is worst case
'''

timesFixed = []
for i in range(35):
    time = timeit.timeit(lambda: fibMemo(i), number = 1)
    timesFixed.append(time)
print(timesFixed)

timesBad = []
for i in range(35):
    time = timeit.timeit(lambda: fib(i), number = 1)
    timesBad.append(time)
print(timesBad)

def doPlot(values):
    plt.plot(values)
    plt.xlabel("Number")
    plt.ylabel("Time taken")
    plt.show()

doPlot(timesFixed)
doPlot(timesBad)