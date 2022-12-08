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
from statistics import NormalDist
from utils import print_util as cprint


def uniform_density(a, b, x):
    if a <= x <= b:
        return cprint.rounded(1 / (b-a))
    else:
        return 0


def uniform_max(a, b, x):
    if x < a:
        return 0
    elif a <= x <= b:
        return cprint.rounded((x-a) / (b-a))
    else:  # x > b
        return 1


def uniform_mean(a, b):
    return cprint.rounded((a+b) / 2)


def uniform_var(a, b):
    return cprint.rounded((b-a)**2 / 12)


def exponential_max(lam, x):
    if x >= 0:
        return cprint.rounded(1 - math.e**(-lam * x))
    else:
        return 0


def exponential_mean(lam):
    return cprint.rounded(1 / lam)


def exponential_var(lam):
    return cprint.rounded(1 / lam**2)


def normal_max(mu, sigma, x):
    return cprint.rounded(NormalDist(mu=mu, sigma=sigma).cdf(x))


def normal_mean(mu):
    return cprint.rounded(mu)


def normal_var(sigma):
    return cprint.rounded(sigma**2)
