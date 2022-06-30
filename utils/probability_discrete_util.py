import math


def rounded(n):
    result = round(n, 3)
    if result % 1 == 0:
        return int(result)
    else:
        return float(result)


def fac(x):
    # Fakultät
    return math.factorial(x)


def binomial(n, k):
    # Binomialkoeffizient
    return fac(n) / (fac(k) * fac(n-k))


def bernoulli_distributed(p):
    q = 1 - p
    return [[1, p], [0, q]]


def bernoulli_expect(p):
    return p


def bernoulli_var(p):
    q = 1 - p
    return rounded(p * q)


def binomial_distributed(n, p):
    # returns array with all binomial distributed values for 0 to n
    # the first element represent the possible t values
    lst = []
    q = 1 - p
    if n > 0:
        for t in range(0, n+1):
            lst.append([t, rounded(binomial(n, t) * p**t * q**(n-t))])
    return lst


def binomial_distributed_x(n, p, x):
    result = 0
    q = 1 - p
    if n > 0:
        result = binomial(n, x) * p**x * q**(n-x)
    return rounded(result)


def binomial_expect(n, p):
    return rounded(n * p)


def binomial_var(n, p):
    return rounded(n * p * (1 - p))


def binomial_min(lst, x):
    result = 0
    for pair in lst:
        if pair[0] >= x:
            result += pair[1]
    return rounded(result)


def binomial_max(lst, x):
    result = 0
    for pair in lst:
        if pair[0] <= x:
            result += pair[1]
    return rounded(result)


def binomial_min_max(lst, x, y):
    result = 0
    for pair in lst:
        if x <= pair[0] <= y:
            result += pair[1]
    return rounded(result)


def geom_distributed(x, p):
    q = 1 - p
    return rounded(p * q**(x - 1))


def geom_expect(p):
    return rounded(1 / p)


def geom_var(p):
    return rounded((1 - p) / math.sqrt(p))


def poisson_distributed(x, lbd):
    if x >= 0:
        return rounded(lbd**x / fac(x) * math.exp(-lbd))
    else:
        return 0
