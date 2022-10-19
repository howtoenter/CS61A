from subprocess import CalledProcessError


def print_all(x):
    print(x)
    return print_all

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum

def pirate(arggg):
    print('matey')
    def plunder(arggg):
        return arggg
    return plunder

def add(x, y):
    return x + y

def square(x):
    return x * x

def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)   #understand?

def trace1(fn):
    """
    Returns a version of fn that first print before it is called
    fn - a function of 1 argument
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

# @trace1
def square(x):
    return x * x
square = trace1(square)

@trace1
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k),k + 1
    return total
