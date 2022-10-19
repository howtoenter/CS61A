
"""
def max_subseq_sum():
    this_sum, max_sum, first, last, judge = 0, 0, 0, 0, 0
    for i in range(n):
        if a[i] > 0:
            judge = 1
        this_sum += a[i]
        if this_sum > max_sum:
            max_sum = this_sum
            last = a[i]
        elif this_sum <= 0:
            this_sum = 0
    if judge == 0:
        first, last = a[0], a[n-1]
    return max_sum, first, last

maxsum, first, last = max_subseq_sum()
print(maxsum, first, last)
"""

"""
def max_subseq_sum1():
    max_sum, first, last, judge = 0, 0, 0, 0
    for i in range(n):
        this_sum = 0
        if a[i] >= 0:
            judge = 1
        for j in range(i, n):
            this_sum += a[j]
            if this_sum > max_sum:
                max_sum = this_sum
                first, last = a[i], a[j]
    if judge == 0:
        first, last = a[0], a[n-1]
    return max_sum, first, last

maxsum, first, last = max_subseq_sum1()
print(maxsum, first, last)
"""

n = int(input())
a = list(map(int, input().split()))
def max_subseq_sum():
    this_sum, max_sum, first, last, tempfirst, judge = 0, 0, 0, 0, 0, 0
    for i in range(n):
        if a[i] >= 0:
            judge = 1
        this_sum += a[i]
        if this_sum <= 0:
            this_sum = 0
            if i != n-1:
                tempfirst = a[i+1]
        if this_sum > max_sum:
            max_sum = this_sum
            first, last = tempfirst, a[i]
    if judge ==0:
        first, last = a[0], a[n-1]
    return max_sum, first, last
maxsum, first, last = max_subseq_sum()
print(maxsum, first, last)
