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
from utils import print_util as cprint


def fac(x):
    # Fakultät
    return cprint.rounded(math.factorial(x))


def binomial(n, k):
    # Binomialkoeffizient
    return cprint.rounded(fac(n) / (fac(k) * fac(n-k)))


def p_n(n):
    # P(n, n) = n!
    return fac(n)


def p_n_k(n, k):
    # P(n, k) = n! / (n-k)!
    return cprint.rounded(fac(n) / fac(n-k))


def p_w(n, k):
    # P^W(n, k) = n^k
    return cprint.rounded(n**k)


def c_n_k(n, k):
    # C(n, k) = (n über k)
    return binomial(n, k)


def c_w(n, k):
    # C^W(n, k) = ((n+k-1) über k)
    return binomial(n+k-1, k)


def laplace(n, k):
    return cprint.rounded(k / n, -1)


def pdf(lst1, lst2, x):
    for i in range(len(lst1)):
        if lst1[i] == x:
            return cprint.rounded(lst2[i])
    return 0


def cdf(lst1, lst2, x):
    sigma = 0
    for i in range(len(lst1)):
        sigma += lst2[i]
        if lst1[i] == x:
            return cprint.rounded(sigma)
    return 0


def mean(lst1, lst2, decimals=-1):
    products = [.0] * len(lst1)
    for i in range(len(products)):
        products[i] = lst1[i] * lst2[i]
    return cprint.rounded(sum(products), decimals)


def var(lst1, lst2, decimals=-1):
    products = [.0] * len(lst1)
    for i in range(len(products)):
        products[i] = lst1[i]**2 * lst2[i]
    return cprint.rounded(sum(products) - mean(lst1, lst2)**2, decimals)


def std(lst1, lst2):
    return cprint.rounded(math.sqrt(var(lst1, lst2, False)), decimals=3)


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
    return cprint.rounded(p * q)


def bernoulli_std(p):
    return cprint.rounded(math.sqrt(bernoulli_var(p)), decimals=4)


def geom_pdf(p, x):
    if x >= 1:
        q = 1 - p
        return cprint.rounded(p * q**(x - 1))
    else:
        return 0


def geom_cdf(p, x):
    if x >= 1:
        q = 1 - p
        return cprint.rounded(1 - q**math.floor(x))
    else:
        return 0


def geom_mean(p):
    return cprint.rounded(1 / p)


def geom_var(p):
    return cprint.rounded((1 - p) / p**2)


def geom_std(p):
    return cprint.rounded(math.sqrt(geom_var(p)), decimals=4)


def binomial_distribution(n, p):
    # returns array with all binomial distributed values for 0 to n
    # the first element represent the possible k values
    lst = []
    if n >= 0:
        q = 1 - p
        for t in range(0, n+1):
            lst.append([t, cprint.rounded(binomial(n, t) * p**t * q**(n-t))])
    return lst


def binomial_pdf(n, p, x):
    if n >= 0:
        q = 1 - p
        return cprint.rounded(binomial(n, x) * p**x * q**(n-x))
    else:
        return 0


def binomial_cdf(n, p, x):
    if x < 0:
        return 0
    elif 0 <= x <= n:
        sigma = 0
        for k in range(math.floor(x) + 1):
            sigma += binomial_pdf(n, p, k)
        return cprint.rounded(sigma)
    else:  # x > n
        return 1


def binomial_mean(n, p):
    return cprint.rounded(n * p)


def binomial_var(n, p):
    return cprint.rounded(n * p * (1 - p))


def binomial_std(n, p):
    return cprint.rounded(math.sqrt(binomial_var(n, p)), decimals=4)


def poisson_pdf(lam, x):
    if x >= 0:
        return cprint.rounded((lam**x / fac(x)) * math.exp(-lam))
    else:
        return 0


def poisson_cdf(lam, x):
    if x >= 0:
        sigma = 0
        for k in range(math.floor(x) + 1):
            sigma += lam**k / fac(k)
        return cprint.rounded(math.exp(-lam) * sigma)
    else:
        return 0


def poisson_std(lam):
    return cprint.rounded(math.sqrt(lam), decimals=4)
