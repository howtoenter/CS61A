def if_(c, t, f):
    if c:
        return t
    else:
        return f

def real_sqrt(x):
    return if_(x > 0, sqrt(x), 0.0)
