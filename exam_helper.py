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

from utils import statistics_util as statistics
from utils import probability_discrete_util as probability_discrete
from utils import probability_continuous_util as probability_continuous
from utils import input_util as cinput
from utils import print_util as cprint

list1 = None
list2 = None


def input_list(save_in_lst1=True):
    try:
        lst = list(map(int, cinput.string().split(" ")))
        if save_in_lst1:
            global list1
            list1 = lst
        else:
            global list2
            list2 = lst
        return lst
    except ValueError:
        cinput.invalid("Nur ganze Zahlen (getrennt durch Leerzeichen) zulässig")
        return input_list(save_in_lst1)


def mean_median_mode_quartile_iqr_span_var_std():
    if list1 is None:
        print("Liste eingeben:")
        lst = input_list()
    else:
        lst = list1
    print("Arithmetisches Mittel:", cprint.yellow_bold(statistics.mean(lst)))
    print("Median:", cprint.yellow_bold(statistics.median(lst)))
    mode = statistics.mode(lst)
    if isinstance(mode, list) and len(lst) > 1:
        print("Modalwerte:", cprint.yellow_bold(mode))
    else:
        print("Modalwert:", cprint.yellow_bold(mode))
    print("25%-Quartil:", cprint.yellow_bold(statistics.quantile(lst, 0.25)))
    print("50%-Quartil:", cprint.yellow_bold(statistics.quantile(lst, 0.50)))
    print("75%-Quartil:", cprint.yellow_bold(statistics.quantile(lst, 0.75)))
    print("Interquartilabstand:", cprint.yellow_bold(statistics.iqr(lst)))
    print("Spannweite:", cprint.yellow_bold(statistics.span(lst)))
    print("Empirische Varianz:", cprint.yellow_bold(statistics.var(lst)))
    print("Empirische Standardabweichung:", cprint.yellow_bold(statistics.std(lst)))


def quantile():
    if list1 is None:
        print("Liste für Quantil eingeben:")
        lst = input_list()
    else:
        lst = list1
    print("Anteil p als Dezimalzahl eingeben:")
    pct = cinput.percentage(False)
    print(str(pct) + "%-Quantil:", cprint.yellow_bold(statistics.quantile(lst, pct * 0.01)))


def corrcoef_covar():
    if list1 is None or list2 is None:
        print("1. Liste für empirischen Korrelationskoeffizienten und empirische Kovarianz eingeben:")
        lst1 = input_list()
        print("2. Liste für empirischen Korrelationskoeffizienten und empirische Kovarianz eingeben:")
        lst2 = input_list(False)
    else:
        lst1 = list1
        lst2 = list2
    print("Empirischer Korrelationskoeffizient:", cprint.yellow_bold(statistics.corrcoef(lst1, lst2)))
    print("Empirische Kovarianz:", cprint.yellow_bold(statistics.covar(lst1, lst2)))


def det():
    if list1 is None or list2 is None:
        print("1. Liste für Bestimmtheitsmaß eingeben:")
        lst1 = input_list()
        print("2. Liste für Bestimmtheitsmaß eingeben:")
        lst2 = input_list(False)
    else:
        lst1 = list1
        lst2 = list2
    print("Bestimmtheitsmaß:", cprint.yellow_bold(statistics.det(lst1, lst2)))


def plot_lin_regress():
    if list1 is None or list2 is None:
        print("1. Liste für lineare Regressionsfunktion eingeben:")
        lst1 = input_list()
        print("2. Liste für lineare Regressionsfunktion eingeben:")
        lst2 = input_list(False)
    else:
        lst1 = list1
        lst2 = list2
    print("Beschriftung der X-Achse eingeben:")
    lbl_x = cinput.string()
    print("Beschriftung der Y-Achse eingeben:")
    lbl_y = cinput.string()
    print("Lineare Regressionsfunktion wird geplottet...")
    statistics.plot_lin_regress(lst1, lst2, lbl_x, lbl_y)


def frequency():
    global list1
    global list2

    print("Welche Häufigkeiten sollen berechnet werden?\n" +
          cprint.bold(1) + " Absolute Häufigkeiten\n" +
          cprint.bold(2) + " Relative Häufigkeiten\n" +
          cprint.bold(3) + " Kumulierte Häufigkeiten\n" +
          cprint.bold(4) + " Funktionen zu beschreibender Statistik\n" +
          cprint.bold(5) + " Hauptmenü")

    answer = cinput.integer(1, 5)

    if (answer == 1 or answer == 2 or answer == 3) and list1 is None:
        print("Liste für Häufigkeiten eingeben:")
        lst = input_list()
    else:
        lst = list1

    match answer:
        case 1:
            print("Absolute Häufigkeiten:", cprint.yellow_bold(statistics.abs_frequency(lst)))
        case 2:
            print("Relative Häufigkeiten:", cprint.yellow_bold(statistics.rel_frequency(lst)))
        case 3:
            print("Kumulierte Häufigkeiten:", cprint.yellow_bold(statistics.cum_frequency(lst)))
        case 4:
            functions_statistics()
        case 5:
            menu_main()

    if answer == 1 or answer == 2 or answer == 3:
        print(cprint.blue_bold("\nOptionen:\n") +
              cprint.bold(1) + " Andere Häufigkeiten ausrechnen\n" +
              cprint.bold(2) + " Funktionen zu beschreibender Statistik\n" +
              cprint.bold(3) + " Hauptmenü")

        match cinput.integer(1, 3):
            case 1:
                frequency()
            case 2:
                print("Werte beibehalten?\n" +
                      cprint.bold(1) + " Ja\n" +
                      cprint.bold(2) + " Nein")
                if cinput.integer(1, 2) == 2:
                    list1 = None
                    list2 = None
                functions_statistics()
            case 3:
                menu_main()


def combination():
    elements_all = False
    elements_sorted = False
    elements_repetition = False

    print("Werden alle Elemente angeordnet?\n" +
          cprint.bold(1) + " Ja\n" +
          cprint.bold(2) + " Nein")
    match cinput.integer(1, 2):
        case 1:
            elements_all = True
        case 2:
            elements_all = False

    if not elements_all:
        print("Spielt die Reihenfolge eine Rolle?\n" +
              cprint.bold(1) + " Ja\n" +
              cprint.bold(2) + " Nein")
        match cinput.integer(1, 2):
            case 1:
                elements_sorted = True
            case 2:
                elements_sorted = False

        print("Sind Wiederholungen erlaubt?\n" +
              cprint.bold(1) + " Ja\n" +
              cprint.bold(2) + " Nein")
        match cinput.integer(1, 2):
            case 1:
                elements_repetition = True
            case 2:
                elements_repetition = False

    print("Gesamtmenge n eingeben:")
    n = cinput.integer(0, None)
    k = 0
    if not elements_all:
        print("Auswahl k eingeben:")
        k = cinput.integer(0, None)

    if elements_all:
        result = probability_discrete.fac(n)
        print("Permutation ohne Wiederholung (z.B. CDs im Regal):", cprint.yellow_bold(result))
        print("Anzahl der k-Permutationen aus einer Menge mit n Elementen ohne Wiederholungen")
        print("Formel: P(n, n) = n!")
    elif not elements_all and elements_sorted and not elements_repetition:
        result = probability_discrete.fac(n) / probability_discrete.fac(n - k)
        print("Variation ohne Wiederholung (z.B. Podestplätze):", cprint.yellow_bold(result))
        print("Anzahl der k-Permutationen aus einer Menge mit n Elementen ohne Wiederholungen")
        print("Formel: C(n, k) = n! / (n-k)!")
    elif not elements_all and elements_sorted and elements_repetition:
        result = n**k
        print("Variation mit Wiederholung (z.B. Passwörter):", cprint.yellow_bold(result))
        print("Anzahl der k-Permutationen aus einer Menge mit n Elementen mit Wiederholungen")
        print("Formel: P^W(n, k) = n^k")
    elif not elements_all and not elements_sorted and not elements_repetition:
        result = probability_discrete.binomial(n, k)
        print("Kombination ohne Wiederholung (z.B. Lotto):", cprint.yellow_bold(result))
        print("Anzahl der möglichen Kombinationen von k Elementen aus einer Menge mit n Elementen ohne Wiederholungen")
        print("Formel: C(n, k) = Binomialkoeffizient (n über k)")
    elif not elements_all and not elements_sorted and elements_repetition:
        numerator = probability_discrete.fac(n + k - 1)
        denominator = probability_discrete.fac(k) * probability_discrete.fac(n - 1)
        result = int(numerator / denominator)
        print("Kombination mit Wiederholung (z.B. Gummibärchen-Orakel):", cprint.yellow_bold(result))
        print("Anzahl der möglichen Kombinationen von k Elementen aus einer Menge mit n Elementen mit Wiederholungen")
        print("Formel: C^W(n, k) = Binomialkoeffizient ((n+k-1) über k)")


def bernoulli_distributed(p=None):
    jump_to_options = p is not None

    if p is None:
        print("Erfolgswahrscheinlichkeit p als Dezimalzahl oder Bruch eingeben:")
        p = cinput.percentage()

    if not jump_to_options:
        print(cprint.bold("Bernoulli-Verteilung: X ~ Ber({})".format(p)))
        for pair in probability_discrete.bernoulli_distribution(p):
            print("P(X = {}) =".format(pair[0]), cprint.yellow_bold(pair[1]))
        print("E[X] =", cprint.yellow_bold(probability_discrete.bernoulli_expect(p)))
        print("Var[X] =", cprint.yellow_bold(probability_discrete.bernoulli_var(p)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(exakt n Versuche bis zum ersten Erfolg)\n" +
          cprint.bold(2) + " Funktion erneut verwenden\n" +
          cprint.bold(3) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(4) + " Hauptmenü")

    match cinput.integer(1, 4):
        case 1:
            print("Anzahl Versuche n bis zum ersten Erfolg für P(X = n) eingeben:")
            n = cinput.float_rounded(False)
            print("P(X = {}) =".format(n), cprint.yellow_bold(probability_discrete.bernoulli_distributed(p, n)))
            bernoulli_distributed(p)
        case 2:
            bernoulli_distributed()
        case 3:
            functions_probability_discrete()
        case 4:
            menu_main()


def binomial_distributed(n=None, p=None):
    jump_to_options = n is not None and p is not None

    if n is None:
        print("Anzahl Versuche n eingeben:")
        n = int(input())
    if p is None:
        print("Wahrscheinlichkeit p als Dezimalzahl oder Bruch eingeben:")
        p = cinput.percentage()

    if not jump_to_options:
        print(cprint.bold("Binomial-Verteilung: X ~ Bin({}, {})".format(n, p)))
        for pair in probability_discrete.binomial_distribution(n, p):
            print("P(X = {}) =".format(pair[0]), cprint.yellow_bold(pair[1]))
        print("E[X] =", cprint.yellow_bold(probability_discrete.binomial_expect(n, p)))
        print("Var[X] =", cprint.yellow_bold(probability_discrete.binomial_var(n, p)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(exakt x)\n" +
          cprint.bold(2) + " P(mindestens x)\n" +
          cprint.bold(3) + " P(höchstens x)\n" +
          cprint.bold(4) + " P(mindestens x und höchstens y)\n" +
          cprint.bold(5) + " Funktion erneut verwenden\n" +
          cprint.bold(6) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(7) + " Hauptmenü")

    match cinput.integer(1, 7):
        case 1:
            print("Anzahl erfolgreiche Versuche x für P(X = x) eingeben:")
            x = cinput.integer(0, n)
            print("P(X = {}) =".format(x), cprint.yellow_bold(probability_discrete.binomial_distributed(n, p, x)))
            binomial_distributed(n, p)
        case 2:
            print("Mindestanzahl erfolgreiche Versuche x für P(X >= x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X >= {}) =".format(x), cprint.yellow_bold(probability_discrete.binomial_min(n, p, x)))
            binomial_distributed(n, p)
        case 3:
            print("Höchstanzahl erfolgreiche Versuche x für P(X <= x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X <= {}) =".format(x), cprint.yellow_bold(probability_discrete.binomial_max(n, p, x)))
            binomial_distributed(n, p)
        case 4:
            print("x (mindestens) eingeben:")
            x = cinput.integer(0, None)
            print("y (höchstens) eingeben:")
            y = cinput.integer(0, None)
            print("P({} <= X >= {}) =".format(x, y),
                  cprint.yellow_bold(probability_discrete.binomial_min_max(n, p, x, y)))
            binomial_distributed(n, p)
        case 5:
            binomial_distributed()
        case 6:
            functions_probability_discrete()
        case 7:
            menu_main()


def geom_distributed(p=None):
    jump_to_options = p is not None

    if p is None:
        print("Wahrscheinlichkeit p als Dezimalzahl oder Bruch eingeben:")
        p = cinput.percentage()

    if not jump_to_options:
        print("Anzahl Versuche x für P(X = x) eingeben:")
        x = cinput.float_rounded(False)
        print(cprint.bold("Geometrische Verteilung: X ~ geom({})".format(p)))
        print("P(X = {}) =".format(x), cprint.yellow_bold(probability_discrete.geom_distributed(p, x)))
        print("E[X] =", cprint.yellow_bold(probability_discrete.geom_expect(p)))
        print("Var[X] =", cprint.yellow_bold(probability_discrete.geom_var(p)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(exakt x)\n" +
          cprint.bold(2) + " P(höchstens x)\n" +
          cprint.bold(3) + " Funktion erneut verwenden\n" +
          cprint.bold(4) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(5) + " Hauptmenü")

    match cinput.integer(1, 5):
        case 1:
            print("Anzahl Versuche x für P(X = x) eingeben:")
            x = cinput.float_rounded(False)
            print("P(X = {}) =".format(x), cprint.yellow_bold(probability_discrete.geom_distributed(p, x)))
            geom_distributed(p)
        case 2:
            print("Höchstanzahl Versuche x für P(X <= x) eingeben:")
            x = cinput.float_rounded(False)
            print("P(X <= {}) =".format(x), cprint.yellow_bold(probability_discrete.geom_max(p, x)))
            geom_distributed(p)
        case 3:
            geom_distributed()
        case 4:
            functions_probability_discrete()
        case 5:
            menu_main()


def poisson_distributed(lbd=None):
    jump_to_options = lbd is not None

    if lbd is None:
        print("Durchschnittliche Auftrittsrate λ eingeben:")
        lbd = cinput.float_rounded(True)

    if not jump_to_options:
        print("Anzahl Vorkommnisse x für P(X = x) eingeben:")
        x = cinput.float_rounded(False)
        print(cprint.bold("Poisson-Verteilung: X ~ Po({})".format(lbd)))
        print("P(X = {}) =".format(x), cprint.yellow_bold(probability_discrete.poisson_distributed(lbd, x)))
        print("E[X] = λ =", cprint.yellow_bold(lbd))
        print("Var[X] = λ =", cprint.yellow_bold(lbd))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(exakt x)\n" +
          cprint.bold(2) + " P(höchstens x)\n" +
          cprint.bold(3) + " Funktion erneut verwenden\n" +
          cprint.bold(4) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(5) + " Hauptmenü")

    match cinput.integer(1, 5):
        case 1:
            print("Anzahl Vorkommnisse x für P(X = x) eingeben:")
            x = cinput.float_rounded(False)
            print("P(X = {}) =".format(x), cprint.yellow_bold(probability_discrete.poisson_distributed(lbd, x)))
            poisson_distributed(lbd)
        case 2:
            print("Höchstanzahl Vorkommnisse x für P(X <= x) eingeben:")
            x = cinput.float_rounded(False)
            print("P(X <= {}) =".format(x), cprint.yellow_bold(probability_discrete.poisson_max(lbd, x)))
            poisson_distributed(lbd)
        case 3:
            poisson_distributed()
        case 4:
            functions_probability_discrete()
        case 5:
            menu_main()


def uniform_distributed(a=None, b=None):
    jump_to_options = a is not None and b is not None

    if a is None:
        print("Minimaler Wert a eingeben:")
        a = cinput.float_rounded(False)
    if b is None:
        print("Maximaler Wert b eingeben:")
        b = cinput.float_rounded(False)

    if not jump_to_options:
        print(cprint.bold("Gleichverteilung: X ~ U({}, {})".format(a, b)))
        print("E[X] =", cprint.yellow_bold(probability_continuous.uniform_expect(a, b)))
        print("Var[X] =", cprint.yellow_bold(probability_continuous.uniform_var(a, b)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(höchstens x)\n" +
          cprint.bold(2) + " Funktion erneut verwenden\n" +
          cprint.bold(3) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(4) + " Hauptmenü")

    match cinput.integer(1, 4):
        case 1:
            print("Höchstwert x für P(X <= x) eingeben:")
            x = cinput.float_rounded(False)
            print("P(X <= {}) =".format(x), cprint.yellow_bold(probability_continuous.uniform_max(a, b, x)))
            uniform_distributed(a, b)
        case 2:
            poisson_distributed()
        case 3:
            functions_probability_discrete()
        case 4:
            menu_main()


def probability_calculation(called_from_discrete):
    if called_from_discrete:
        back = " Funktionen zu diskreter Wahrscheinlichkeitstheorie"
    else:
        back = " Funktionen zu kontinuierlicher Wahrscheinlichkeitstheorie"

    print(cprint.blue_bold("Kalkulationshilfe:\n") +
          cprint.bold(1) + " Mindestens x\n" +
          cprint.bold(2) + " Mehr als x\n" +
          cprint.bold(3) + " Weniger als x\n" +
          cprint.bold(4) + " x oder y\n" +
          cprint.bold(5) + back + "\n" +
          cprint.bold(6) + " Hauptmenü")

    match cinput.integer(1, 6):
        case 1:
            print("Wert x für P(X >= x) eingeben:")
            x = cinput.float_rounded()
            print("P(X >= {}) =".format(x), cprint.yellow_bold("1 - P(X <= {})".format(x-1)))
        case 2:
            print("Wert x für P(X > x) eingeben:")
            x = cinput.float_rounded()
            print("P(X > {}) =".format(x), cprint.yellow_bold("1 - P(X <= {})".format(x)))
        case 3:
            print("Wert x für P(X < x) eingeben:")
            x = cinput.float_rounded()
            print("P(X < {}) =".format(x), cprint.yellow_bold("P(X <= {})".format(x-1)))
        case 4:
            print("Wert x für P(X = x ∨ X = y) eingeben:")
            x = cinput.float_rounded()
            print("Wert y für P(X = x ∨ X = y) eingeben:")
            y = cinput.float_rounded()
            print("P(X = {} ∨ X = {}) =".format(x, y), cprint.yellow_bold("P(X = {}) + P(X = {})".format(x, y)))
        case 5:
            if called_from_discrete:
                functions_probability_discrete()
            else:
                functions_probability_continuous()
        case 6:
            menu_main()


def menu_main(menu_code=0):
    global list1
    global list2
    list1 = None  # reset statistic lists
    list2 = None

    if menu_code == 0:
        print(cprint.blue_bold("Hauptmenü:\n") +
              cprint.bold(1) + " Beschreibende Statistik\n" +
              cprint.bold(2) + " Diskrete Wahrscheinlichkeitstheorie\n" +
              cprint.bold(3) + " Kontinuierliche Wahrscheinlichkeitstheorie")
        menu_code = cinput.integer(1, 3)

    match menu_code:
        case 1:
            functions_statistics()
        case 2:
            functions_probability_discrete()
        case 3:
            functions_probability_continuous()


def functions_statistics(func_code=0):
    global list1
    global list2

    if func_code == 0:
        print(cprint.blue_bold("Beschreibende Statistik:\n") +
              cprint.bold(1) + " Arithmetisches Mittel, Median, Modalwert, Quartile, Interquartilabstand,"
                               " Spannweite, Empirische Varianz & Standardabweichung\n" +
              cprint.bold(2) + " Quantil\n" +
              cprint.bold(3) + " Empirischer Korrelationskoeffizient & Kovarianz\n" +
              cprint.bold(4) + " Bestimmtheitsmaß\n" +
              cprint.bold(5) + " Lineare Regressionsfunktion\n" +
              cprint.bold(6) + " Häufigkeiten\n" +
              cprint.bold(7) + " Hauptmenü")
        func_code = cinput.integer(1, 7)

    match func_code:
        case 1:
            mean_median_mode_quartile_iqr_span_var_std()
        case 2:
            quantile()
        case 3:
            corrcoef_covar()
        case 4:
            det()
        case 5:
            plot_lin_regress()
        case 6:
            frequency()
        case 7:
            menu_main()

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " Funktion mit anderen Werten wiederholen\n" +
          cprint.bold(2) + " Funktionen zu beschreibender Statistik\n" +
          cprint.bold(3) + " Hauptmenü")

    match cinput.integer(1, 3):
        case 1:
            list1 = None
            list2 = None
            functions_statistics(func_code)
        case 2:
            print("Werte beibehalten?\n" +
                  cprint.bold(1) + " Ja\n" +
                  cprint.bold(2) + " Nein")
            if cinput.integer(1, 2) == 2:
                list1 = None
                list2 = None
            functions_statistics()
        case 3:
            menu_main()


def functions_probability_discrete(func_code=0):
    if func_code == 0:
        print(cprint.blue_bold("Diskrete Wahrscheinlichkeitstheorie:\n") +
              cprint.bold(1) + " Kombinatorik\n" +
              cprint.bold(2) + " Bernoulli-Verteilung (genau zwei mögliche Ausgänge)\n" +
              cprint.bold(3) + " Binomial-Verteilung (Anzahl erfolgreicher Versuche)\n" +
              cprint.bold(4) + " Geometrische Verteilung (Wartezeiten bis zum ersten Erfolg)\n" +
              cprint.bold(5) + " Poisson-Verteilung (Häufigkeit eines Ereignisses über Zeitraum betrachtet)\n" +
              cprint.bold(6) + " Kalkulationshilfe (mindestens, mehr als, weniger als, oder)\n" +
              cprint.bold(7) + " Hauptmenü")
        func_code = cinput.integer(1, 6)

    match func_code:
        case 1:
            combination()
        case 2:
            bernoulli_distributed()
        case 3:
            binomial_distributed()
        case 4:
            geom_distributed()
        case 5:
            poisson_distributed()
        case 6:
            probability_calculation(True)
        case 7:
            menu_main()

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " Funktion erneut verwenden\n" +
          cprint.bold(2) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(3) + " Hauptmenü")

    match cinput.integer(1, 3):
        case 1:
            functions_probability_discrete(func_code)
        case 2:
            functions_probability_discrete()
        case 3:
            menu_main()


def functions_probability_continuous(func_code=0):
    if func_code == 0:
        print(cprint.blue_bold("Kontinuierliche Wahrscheinlichkeitstheorie:\n") +
              cprint.bold(1) + " Gleichverteilung\n" +
              cprint.bold(2) + " Exponentialverteilung (Dauer zufälliger Zeitintervalle)\n" +
              cprint.bold(3) + " Normalverteilung\n" +
              cprint.bold(4) + " Kalkulationshilfe (mindestens, mehr als, weniger als, oder)\n" +
              cprint.bold(5) + " Hauptmenü")
        func_code = cinput.integer(1, 5)

    match func_code:
        case 1:
            uniform_distributed()
        case 2:
            uniform_distributed()
        case 3:
            uniform_distributed()
        case 4:
            probability_calculation(False)
        case 5:
            menu_main()

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " Funktion erneut verwenden\n" +
          cprint.bold(2) + " Funktionen zu kontinuierlicher Wahrscheinlichkeitstheorie\n" +
          cprint.bold(3) + " Hauptmenü")

    match cinput.integer(1, 3):
        case 1:
            functions_probability_continuous(func_code)
        case 2:
            functions_probability_continuous()
        case 3:
            menu_main()


print(cprint.yellow("Viel Erfolg!\n"))
menu_main()
