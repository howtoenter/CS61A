from tkinter import Y


def split(n):
    return n // 10, n % 10
def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last
    
def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(last * 2)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def cascade(n):
    print(n)
    if n > 10:
        cascade(n//10)
        print(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n : f_then_g(grow, print, n//10)
shrink = lambda n : f_then_g(print, shrink, n//10)

y = "y"
h = y 
def y(y):
    h == "h"
    if y == h:
        return y + "i"
    y = lambda y:y(h)
    return lambda h: y(h)
y = y(y)(y)

def keep_ints(cond, n):
    for i in range(1, n):
        if cond(i):
            print(i)

def is_even(x):
    return x % 2 == 0

def make_keeper(n):
    def do_keep(cond):
        for i in range(1,n):
            if cond(i):
                print(i)
    return do_keep

def print_delayed(x):
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

def print_n(n):
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print

def yes(no):
    yes = 'no'
    return no

no = 'no'    

def no(no):
    return no + yes(no)

yes = yes(yes)(no)('ok')