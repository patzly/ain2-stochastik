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


def fac(x):
    # Fakultät
    return math.factorial(x)


def binomial(n, k):
    # Binomialkoeffizient
    return fac(n) / (fac(k) * fac(n-k))


def p_n(n):
    # P(n, n) = n!
    return fac(n)


def p_n_k(n, k):
    # P(n, k) = n! / (n-k)!
    return fac(n) / fac(n-k)


def p_w(n, k):
    # P^W(n, k) = n^k
    return n**k


def c_n_k(n, k):
    # C(n, k) = (n über k)
    return binomial(n, k)


def c_w(n, k):
    # C^W(n, k) = ((n+k-1) über k)
    return binomial(n+k-1, k)


def laplace(n, k):
    return k / n


def pdf(lst1, lst2, x):
    for i in range(len(lst1)):
        if lst1[i] == x:
            return lst2[i]
    return 0


def cdf(lst1, lst2, x):
    sigma = 0
    for i in range(len(lst1)):
        sigma += lst2[i]
        if lst1[i] == x:
            return sigma
    return 0


def mean(lst1, lst2):
    products = []
    for i in range(len(lst1)):
        products.append(float(lst1[i] * lst2[i]))
    return sum(products)


def var(lst1, lst2):
    products = []
    for i in range(len(lst1)):
        products.append(float(lst1[i]**2 * lst2[i]))
    return sum(products) - mean(lst1, lst2)**2


def std(lst1, lst2):
    return math.sqrt(var(lst1, lst2))


def bernoulli_pdf(p, x):
    if x == 0:
        return p
    elif x == 1:
        q = 1 - p
        return q
    else:
        return 0


def bernoulli_cdf(p, x):
    if x < 0:
        return 0
    elif x <= 0 < 1:
        q = 1 - p
        return q
    else:
        return 1


def bernoulli_mean(p):
    return p


def bernoulli_var(p):
    q = 1 - p
    return p * q


def bernoulli_std(p):
    return math.sqrt(bernoulli_var(p))


def geom_pdf(p, x):
    if x >= 1:
        q = 1 - p
        return p * q**(x - 1)
    else:
        return 0


def geom_cdf(p, x):
    if x >= 1:
        q = 1 - p
        return 1 - q**math.floor(x)
    else:
        return 0


def geom_mean(p):
    return 1 / p


def geom_var(p):
    return (1 - p) / p**2


def geom_std(p):
    return math.sqrt(geom_var(p))


def binomial_pdf(n, p, x):
    if n >= 0:
        q = 1 - p
        return binomial(n, x) * p**x * q**(n-x)
    else:
        return 0


def binomial_cdf(n, p, x):
    if x < 0:
        return 0
    elif 0 <= x <= n:
        sigma = 0
        for k in range(math.floor(x) + 1):
            sigma += binomial_pdf(n, p, k)
        return sigma
    else:  # x > n
        return 1


def binomial_mean(n, p):
    return n * p


def binomial_var(n, p):
    return n * p * (1 - p)


def binomial_std(n, p):
    return math.sqrt(binomial_var(n, p))


def poisson_pdf(lam, x):
    if x >= 0:
        return (lam**x / fac(x)) * math.exp(-lam)
    else:
        return 0


def poisson_cdf(lam, x):
    if x >= 0:
        sigma = 0
        for k in range(math.floor(x) + 1):
            sigma += lam**k / fac(k)
        return math.exp(-lam) * sigma
    else:
        return 0


def poisson_std(lam):
    return math.sqrt(lam)
