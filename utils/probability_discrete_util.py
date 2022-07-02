#  This file is part of Exam Helper.
#
#  Exam Helper is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Exam Helper is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Exam Helper. If not, see <http://www.gnu.org/licenses/>.
#
#  Copyright (c) 2022 by Patrick Zedler

import math


def rounded(n):
    result = round(n, 3)
    if result % 1 == 0:
        return int(result)
    else:
        return float(result)


def fac(x):
    # Fakultät
    return rounded(math.factorial(x))


def binomial(n, k):
    # Binomialkoeffizient
    return rounded(fac(n) / (fac(k) * fac(n-k)))


def p_n(n):
    # P(n, n) = n!
    return fac(n)


def p(n, k):
    # P(n, k) = n! / (n-k)!
    return rounded(fac(n) / fac(n-k))


def p_w(n, k):
    # P^W(n, k) = n^k
    return rounded(n**k)


def c(n, k):
    # C(n, k) = (n über k)
    return binomial(n, k)


def c_w(n, k):
    # C^W(n, k) = ((n+k-1) über k)
    return binomial(n+k-1, k)


def laplace(n, k):
    return rounded(k / n)


def bernoulli_distribution(p):
    return [[1, p], [0, rounded(1-p)]]


def bernoulli_distributed(p, n):
    q = 1 - p
    return rounded((n-1) * q * p)


def bernoulli_expect(p):
    return p


def bernoulli_var(p):
    q = 1 - p
    return rounded(p * q)


def binomial_distribution(n, p):
    # returns array with all binomial distributed values for 0 to n
    # the first element represent the possible k values
    lst = []
    if n >= 0:
        q = 1 - p
        for t in range(0, n+1):
            lst.append([t, rounded(binomial(n, t) * p**t * q**(n-t))])
    return lst


def binomial_distributed(n, p, x):
    if n >= 0:
        q = 1 - p
        return rounded(binomial(n, x) * p**x * q**(n-x))
    else:
        return 0


def binomial_min(n, p, x):
    if x < 0:
        return 0
    elif 0 <= x <= n:
        sigma = 0
        for k in range(math.floor(x), n + 1):
            sigma += binomial_distributed(n, p, k)
        return rounded(sigma)
    else:  # x > n
        return 1


def binomial_max(n, p, x):
    if x < 0:
        return 0
    elif 0 <= x <= n:
        sigma = 0
        for k in range(math.floor(x) + 1):
            sigma += binomial_distributed(n, p, k)
        return rounded(sigma)
    else:  # x > n
        return 1


def binomial_min_max(n, p, x, y):
    if x < 0:
        return 0
    elif 0 <= x <= n:
        sigma = 0
        for k in range(math.floor(x), math.floor(y) + 1):
            sigma += binomial_distributed(n, p, k)
        return rounded(sigma)
    else:  # x > n
        return 1


def binomial_expect(n, p):
    return rounded(n * p)


def binomial_var(n, p):
    return rounded(n * p * (1 - p))


def geom_distributed(p, x):
    if x >= 1:
        q = 1 - p
        return rounded(p * q**(x - 1))
    else:
        return 0


def geom_max(p, x):
    if x >= 1:
        q = 1 - p
        return rounded(1 - q**math.floor(x))
    else:
        return 0


def geom_expect(p):
    return rounded(1 / p)


def geom_var(p):
    return rounded((1 - p) / p**2)


def poisson_distributed(lam, x):
    if x >= 0:
        return rounded(lam**x / fac(x) * math.exp(-lam))
    else:
        return 0


def poisson_max(lam, x):
    if x >= 0:
        sigma = 0
        for k in range(math.floor(x)+1):
            sigma += (lam**k / fac(k))
        return rounded(math.exp(-lam) * sigma)
    else:
        return 0
