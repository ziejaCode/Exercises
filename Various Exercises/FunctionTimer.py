'''
this is small software used to measure the execution time of given method
'''
import time

def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start)/rep

#time_it(print, 1,2,3, sep=' - ', end=' ***\n', rep=5)

def compute_pow1(n, end, start=1):
    # using a for loop
    resutls = [] #empty list to store results of calculation
    for i in range(start, end):        
        resutls.append(n**i)
    return resutls

#print(compute_pow1(2, end=5))

def compute_pow2(n, end, start=1):
    #using list comprehention
    return[n**i for i in range(start, end)]

#print(compute_pow2(2, end=5))

def compute_pow3(n, *, start=1, end):
    #using generators expresion
    return(n**i for i in range(start, end))

#print(list(compute_pow3(2, end=5))) 

print(time_it(compute_pow1, 2, start=0, rep=5, end=2000))