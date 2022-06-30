import numpy as np
import scipy.stats as stats
import math
import matplotlib.pyplot as plt
from statistics import multimode


def mean(lst):
    # Arithmetisches Mittel
    # return np.mean(lst)
    return round(sum(lst) / len(lst), 3)


def median(lst):
    # Median
    return np.median(lst)


def mode(lst):
    # Modalwert
    # return max(lst, key=lst.count)
    modes = multimode(lst)
    if len(modes) == 1:
        return modes[0]
    else:
        return str(modes).replace("[", "").replace("]", "")


def quantile(lst, p):
    # p%-Quantil (p * 100)
    # Formel aus der Vorlesung
    # return np.quantile(lst, p, method='averaged_inverted_cdf')
    # method='averaged_inverted_cdf' works as expected but custom is safer
    # https://github.com/numpy/numpy/issues/13267#issuecomment-482802849
    lst = np.sort(lst)
    n = len(lst)
    pn = int(math.ceil(n*p))-1  # start from first element (np index start is 1)
    if n*p % 1 == 0:
        return (lst[pn] + lst[pn+1]) / 2
    else:
        return lst[pn]


def iqr(lst):
    # Interquartilabstand
    # stats.iqr(lst)
    return quantile(lst, 0.75) - quantile(lst, 0.25)


def span(lst):
    # Spannweite
    return max(lst) - min(lst)


def var(lst):
    # Empirische Varianz
    # Formel aus der Vorlesung
    # return np.var(lst, ddof=1)
    n = len(lst)
    sigma = 0
    for i in lst:
        sigma += (i-mean(lst))**2
    return round(1/(n-1) * sigma, 3)


def std(lst):
    # Empirische Standardabweichung
    # Formel aus der Vorlesung
    # return np.std(lst, ddof=1)
    return round(math.sqrt(var(lst)), 3)


def covar(lst1, lst2):
    # Empirische Kovarianz
    n = len(lst1)
    sigma = 0
    for i in range(0, n):
        sigma += (lst1[i] - mean(lst1)) * (lst2[i] - mean(lst2))
    covariance = (1 / (n - 1)) * sigma
    return round(covariance, 3)


def corrcoef(lst1, lst2):
    # Empirischer Korrelationskoeffizient
    # return stats.pearsonr(lst1, lst2)[0]
    # return np.corrcoef(lst1, lst2) not working as expected
    coefficient = covar(lst1, lst2) / (std(lst1) * std(lst2))
    return round(coefficient, 3)


def det(lst1, lst2):
    # Bestimmheitsmaß
    return corrcoef(lst1, lst2)**2


def plot_lin_regress(lst1, lst2, lbl_x, lbl_y):
    lst1 = np.asarray(lst1)
    lst2 = np.asarray(lst2)
    slope, intercept, r, p, stderr = stats.linregress(lst1, lst2)
    line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'

    fig, ax = plt.subplots()
    ax.plot(lst1, lst2, linewidth=0, marker='s', label='Data points')
    ax.plot(lst1, intercept + slope * lst1, label=line)
    ax.set_xlabel(lbl_x)
    ax.set_ylabel(lbl_y)
    ax.legend(facecolor='white')
    plt.show()


def abs_frequency(lst):
    # returns multidimensional array with number as the first and frequency as the second value
    absolute = []
    if len(lst) > 0:
        arr_sorted = []
        for i in lst:
            arr_sorted.append(i)
        arr_sorted.sort()

        number = arr_sorted[0]
        counter = 0
        for i in arr_sorted:
            if number != i:
                absolute.append([number, counter])
                number = i
                counter = 1
            else:
                counter += 1
        absolute.append([number, counter])
    return absolute


def rel_frequency(lst):
    relative = []
    if len(lst) > 0:
        absolute = abs_frequency(lst)
        ges = 0
        for i in absolute:
            ges += i[1]
        for i in absolute:
            relative.append([i[0], round(i[1]/ges, 3)])
    return relative


def cum_frequency(lst):
    cumulative = []
    if len(lst) > 0:
        rel = rel_frequency(lst)
        kum_counter = 0
        for i in rel:
            kum_counter += i[1]
            cumulative.append([i[0], round(kum_counter, 3)])
    return cumulative
