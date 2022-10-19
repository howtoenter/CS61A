def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    return lambda x: f(x)

def two(f):
    return lambda x: f(f(x))

three = successor(two)

def church_to_int(n):
    f = lambda x: x + 1
    return n(f)(0)

def add_church(m, n):
    return lambda f: lambda x: m(f)(n(f)(x))

def mul_church(m, n):
    return lambda f: m(n(f))

def pow_church(m, n):
    return lambda f: (n(m))(f)
    
