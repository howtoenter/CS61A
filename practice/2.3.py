def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def path(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return path(m-1, n) + path(m, n-1)

#Knapsack

def knap(n, k):
    if n == 0:
        return k == 0
    with_last = knap(n // 10, k - n % 10)
    without_last = knap(n // 10, k)
    return with_last or without_last

#Counting Partitions

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m

def remove(n, digit):
    """Return all digits of non-negative N that are not DIGIT, 
       for some non-negative DIGIT less than 10.
    >>> remove(231, 3)
    21
    >>> remove(243132, 2) 
    4313
    """
    kept, digits = 0, 0

    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + last*10**digits
            digits = digits + 1
    return kept
