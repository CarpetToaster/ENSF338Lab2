import timeit

'''
i)  interpolation can be better than a binary search when there is some exploitable predetermined pattern,
    for example, if the key is expected to be at around 1/4 of the total array, we can set that as 
    the midpoint and expect a return sooner.
    while related to the previous point, we can say another pro to interpolation search over binary 
    
ii) while interpolation search will work just fine if the data isn't uniformly distributed (it still must be sorted)
    however performance may take a hit as it no longer has the predictive advantage it previously had.
    
iii)the pos assignment would change, as it is currently just taking some average (for uniform dist), it would have to be adjusted 
    to match the CDF of said distribution to remaximize the speed.
'''

'''
iv) if data is both arranged randomly and for whatever reason cannot (or shouldn't) be sorted.

v)  linear may outperform binary and interpolation searches when either the array is really short (likely similar performance)
    or when the array is unsorted, in which case it make take longer to sort and search than just to search. This is the case 
    when a search only really needs to occure once. 
    
vi) Not that we can think of; binary and interpolation searches work for what they need to work for, the drawbacks of them
    requiring sorted or correctly distributive arrays just means an extra step may have to be taken, only when it's worth it.

'''