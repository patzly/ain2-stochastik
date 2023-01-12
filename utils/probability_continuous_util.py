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
import scipy.stats as stats


def uniform_cdf(a, b, x):
    if x < a:
        return 0
    elif a <= x <= b:
        return (x-a) / (b-a)
    else:  # x > b
        return 1


def uniform_ppf(a, b, p):
    return stats.uniform.ppf(p, loc=a, scale=b-a)


def uniform_mean(a, b):
    return (a+b) / 2


def uniform_var(a, b):
    return (b-a)**2 / 12


def uniform_std(a, b):
    return math.sqrt(uniform_var(a, b))


def exponential_cdf(lam, x):
    if x >= 0:
        return 1 - math.e**(-lam * x)
    else:
        return 0


def exponential_ppf(lam, p):
    return stats.expon.ppf(p, loc=0, scale=1/lam)


def exponential_mean(lam):
    return 1 / lam


def exponential_var(lam):
    return 1 / lam**2


def exponential_std(lam):
    return math.sqrt(exponential_var(lam))


def normal_cdf(mu, sigma, x):
    return stats.norm.cdf(x, loc=mu,scale=sigma)


def normal_ppf(mu, sigma, x):
    return stats.norm.ppf(x, mu, sigma)


def normal_mean(mu):
    return mu


def normal_var(sigma):
    return sigma**2


def normal_std(sigma):
    return math.sqrt(normal_var(sigma))
