import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd
from utils import statistics_util as stats
from utils import print_util as cprint


def task_1_5():
    alice = [2, 4, 3, 1, 2, 4, 2, 2, 2, 3]
    cprint.magenta('Aufgabe 1.5: An der Fahrradbrücke')
    print('Arithmetisches Mittel:', stats.mean(alice))
    print('Median:', stats.median(alice))
    print('Modalwert:', stats.mode(alice))
    print('10%-Quantil:', stats.quantile(alice, 0.1))
    print('25%-Quantil:', stats.quantile(alice, 0.25))
    print('75%-Quantil:', stats.quantile(alice, 0.75))
    print('Interquartilabstand:', stats.iqr(alice))
    print('Spannweite:', stats.span(alice))
    print()


def task_1_6():
    frank = [25, 10, 30, 25, 35, 25]
    cprint.magenta('Aufgabe 1.6: Taschengeld')
    cprint.cyan('Teilaufgabe 1.6.1')
    print('Arithmetisches Mittel:', stats.mean(frank))
    print('Median:', stats.median(frank))
    print('75%-Quantil:', stats.quantile(frank, 0.75))
    print('Empirische Standardabweichung:', stats.std(frank))
    cprint.cyan('Teilaufgabe 1.6.2')
    print('Spannweite:', stats.span(frank))
    print('Interquartilabstand:', stats.iqr(frank))
    print('25%-Quantil:', stats.quantile(frank, 0.25))
    print()


def task_1_9():
    x = [1, 2, 3, 4, 5, 6]
    y_a = [-1, 0, 0, 0.5, 1, 1.5]
    y_b = [0.5, 0, 0, -1, -1, -1.5]
    y_c = [1, -0.3, -0.2, 0.35, -2.1, -1.6]
    cprint.magenta('Aufgabe 1.9: Punktwolken')
    cprint.cyan('Teilaufgabe 1.9.1')
    print('Korrelationskoeffizient von A:', stats.corrcoef(x, y_a))
    print('Korrelationskoeffizient von B:', stats.corrcoef(x, y_b))
    print('Korrelationskoeffizient von C:', stats.corrcoef(x, y_c))
    print()


def task_1_12():
    duration = [9, 13, 15, 18, 20]
    salary = [18, 37, 61, 125, 59]
    cprint.magenta('Aufgabe 1.12: Ausbildung & Gehälter')
    print('Empirischer Korrelationskoeffizient:\n', stats.corrcoef(duration, salary))
    print('Bestimmtheitsmaß:\n', stats.det(duration, salary))
    print('\n')
    # [[1. 0.70255473]
    # [0.70255473 1.]]

    df = pd.DataFrame(list(zip(duration, salary)), columns=['Ausbildungsdauer', 'Jahresgehalt'])
    # plt.plot(duration, salary)
    sbn.regplot(x='Ausbildungsdauer', y='Jahresgehalt', data=df)
    plt.show()


def task_1_14():
    years = [2018, 2019, 2020, 2021]
    victims = [3275, 3046, 2719, 2564]
    cprint.magenta('Aufgabe 1.14: 3 Key Facts')
    print('\n')

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_ylabel('Verkehrstote')
    ax.set_xlabel('Jahr')
    ax.bar(years, victims)

    df = pd.DataFrame(list(zip(years, victims)), columns=['Jahr', 'Verkehrstote'])
    # plt.plot(duration, salary)
    # sbn.regplot(x='Jahr', y='Verkehrstote', data=df)
    plt.show()


def test():
    data = {'2018': 3275, '2019': 3046, '2020': 2719, '2021': 2564}
    years = list(data.keys())
    victims = list(data.values())
    plt.bar(years, victims, color='maroon', width=0.4)

    plt.xlabel('Jahr')
    plt.ylabel('Anzahl Verkehrstote')
    plt.title('Vekehrsunfälle in Deutschland')
    plt.show()


task_1_5()
task_1_6()
task_1_9()
# task_1_12()
# task_1_14()
# test()
