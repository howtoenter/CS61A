from re import X


def sculptural(ruler ,k):
    if k == 0 or ruler == 0:
        return 0
    a = ruler % 10 + sculptural(ruler//10, k-1) * 10
    b = sculptural(ruler//10, k)
    return max(a, b)
"""
??
tree recursion
1. base case
2. recursive call
"""

from operator import add, mul

def reduce(f, s ,initial):
    """Combine elements of s using f starting with initial

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial, x)
    return initial
    

# Disc04

#1.1
def multiply(m, n):
    if not n:
        return 0
    return m + multiply(m, n-1)

#1.2
def is_prime(n):
    def prime_helper(index):
        if index == n:
            return True
        elif n % index == 0 or n == 1:
            return False
        else:
            return prime_helper(index + 1)
    return prime_helper(2)
        
def fib(n):
    first, second = 0, 1
    if n == 1:
        return first
    else:
        for i in range(n-2):
            first, second = second, first + second
        return second
    
#2.1
def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return count_stair_ways(n-1) + count_stair_ways(n-2)

#2.2
def count_k(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total, i = 0, 1
        while i <= k:
            total += count_k(n-i, k)
            i += 1
        return total
#3
    #   list comprehension: newlist = [expression for item in iterable if condition == True]
def list_comprehension():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if 'a' in x]
    print(newlist)
    
#3.2
def even_weighted(s):
    #return [s[i-1]*(i-1) for i in s if (i-1)%2 == 0]
    return [i*s[i] for i in range(len(s)) if i%2 == 0]

#3.3
def max_products(s):
    if not s:
        return 1
    a = s[0] * max_products(s[2:])
    b = 1 * max_products(s[1:])
    return max(a, b)

#1.Whole Numbers
#a
def check_hole_number(n):
    if n // 10 == 0:
        return True
    return ((n//10)%10) < (n%10) and ((n//10)%10) < ((n//100)%10) and check_hole_number(n//100)
#欣赏，欣赏...

#b
def check_mountain_number(n):
    def helper(x, is_increasing):
        if x // 10 == 0:
            return True
        if is_increasing and (x%10) < ((x//10)%10):
            return helper(x//10, True)
        return (x%10) > ((x//10)%10) and helper(x//10, False)
    return helper(n, True)

# Trees

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


#------------------------------------

from datetime import date
#------------------------------------

#disc05
#1.1
def height(t):
    if is_leaf(t):
        return 0
    return 1 + max([height(branch) for branch in branches(t)])

#1.2
def square_tree(t):
    return tree(label(t)**2, [square_tree(branch) for branch in branches(t)])

#1.3
def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path

def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw
#useless
def make1_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

#Implicit Sequence
def double_and_print(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x 

def letters_generator():
    current = 'a'
    while current < 'd':
        yield current   #yield: return elements of a series
        current = chr(ord(current)+1)

"""
>>>letters = letters_generator()
>>>type(letters)
<class 'generator'>
>>>letters.__next__() 
'a'
>>>letters.__next__()
'b'
"""

def all_pairs(s):
    for item1 in s:
        for item2 in s:
            yield(item1, item2)
"""
>>>list(all_pairs([1, 2, 3]))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
"""

#disc06

def memory(n):
    def helper(f):
        nonlocal n
        return f(n)
    return helper #参数f不直接给出时注意不要带 ()

def nonlocalist():
    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = get
        def get(i):
            if i == 0:
                return value
            return f(i-1)
        return prepend, lambda x: get(x)

def compound(f):
    h = lambda x: x
    def g(x):
        nonlocal h
        # h = (lambda oldh: lambda x: f(oldh(x)))(h)
        h = lambda x, oldh=h: f(oldh(x))#懵逼
        return h(x)
    return g

#Generators
def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s
        
def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

class Account():
    interest = 0.02 #A class attribute
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance
    
class CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
    
class Bank:
    """A bank *has* accounts.

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)
    
    def too_big_to_fail(self):
        return len(self.accounts) > 1
# def deposit_all(winners, amount=5):
#     for account in winners:
#         Account.deposit(account, amount)

def cut(length, width):
    if length == width:
        return 1
    elif length > width:
        return 1 + cut(length - width, width)
    else:
        return 1 + cut(length, width - length)
    
def sums():
    n = input()
    sum = 0
    for i in range(1, int(n)+1):
        temp = i
        while(i != 0):
            last = i % 10
            if last == 2 or last == 0 or last == 1 or last == 9:
                sum += temp
                break
            i = i // 10
    return sum

def combo(a, b):
    if a == 0 or b == 0:
        return a + b
    elif a % 10 == b % 10:
        return combo(a // 10, b // 10) * 10 + a % 10
    else:
        return min(combo(a // 10, b) * 10 + a % 10, 
                   combo(a, b // 10) * 10 + b % 10)
    
class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting

class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'I gather wealth'
    
class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)

class C(B):
    def f(self, x):
        return X
    
    
def generate_subsets():
    subsets = [[]]
    n = 1
    while True:
        yield subsets
        subsets = subsets + [s + [n] for s in subsets]
        n += 1
"""
We start with a base list of subsets. To get the next sequence of subsets, 
we need two things:
    All current subsets will continue to be valid subsets in the future.
    We take all the subsets we currently have, and add the next number. 
    These are also valid subsets.
"""

def sum_paths_tree(t):
    if is_leaf(t):
        yield label(t)
    for b in branches(t):
        for s in sum_paths_tree(b):
            yield s + label(t)

class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, ta):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)
    
class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

"""
We suggest that you approach this problem by first filling out the Email class, then
fill out the register client method of Server, then implement the Client class,
and lastly fill out the send method of the Server class.
"""
class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        client = self.clients[email.recipient_name]
        client.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []

        self.server = server
        self.name = name
        self.server.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)