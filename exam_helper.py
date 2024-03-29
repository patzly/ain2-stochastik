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
        lst = list(map(float, cinput.string().split(" ")))
        if save_in_lst1:
            global list1
            list1 = lst
        else:
            global list2
            list2 = lst
        return lst
    except ValueError:
        cinput.invalid("Nur ganze Zahlen und Dezimalzahlen (getrennt durch Leerzeichen) zulässig")
        return input_list(save_in_lst1)



def input_probabilities(save_in_lst1=True, count=None):
    try:
        lst = cinput.floats_fraction(True, True)
        if count is not None and len(lst) != count:
            if len(lst) == 1:
                lst = [lst[0]] * count
            else:
                cinput.invalid("Es werden genau {} Wahrscheinlichkeiten benötigt".format(count))
                return input_probabilities(save_in_lst1)
        if save_in_lst1:
            global list1
            list1 = lst
        else:
            global list2
            list2 = lst
        return lst
    except ValueError:
        cinput.invalid("Nur ganze Zahlen und Dezimalzahlen (getrennt durch Leerzeichen) zulässig")
        return input_probabilities(save_in_lst1)


def mean_median_mode_quartile_iqr_span_var_std(jump_to_options=False):
    global list1
    global list2

    if not jump_to_options:
        if list1 is None:
            print("Liste eingeben:")
            lst = input_list()
        else:
            lst = list1

        print("Arithmetisches Mittel:", cprint.yellow_bold_rounded(statistics.mean(lst)),
              cprint.magenta("numpy.mean()"))
        print("Median:", cprint.yellow_bold_rounded(statistics.median(lst)), cprint.magenta("numpy.median(lst)"))
        mode = statistics.mode(lst)
        if "," in mode:
            print("Modalwerte:", cprint.yellow_bold(mode), cprint.magenta("statistics.multimode(lst)"))
        else:
            print("Modalwert:", cprint.yellow_bold(mode), cprint.magenta("statistics.multimode(lst)"))
        print("25%-Quartil:", cprint.yellow_bold_rounded(statistics.quantile(lst, 0.25)),
              cprint.magenta("numpy.quantile(lst, p, method='averaged_inverted_cdf')"))
        print("50%-Quartil:", cprint.yellow_bold_rounded(statistics.quantile(lst, 0.50)))
        print("75%-Quartil:", cprint.yellow_bold_rounded(statistics.quantile(lst, 0.75)))
        print("Interquartilabstand:", cprint.yellow_bold_rounded(statistics.iqr(lst)),
              cprint.magenta("statistics.quantile(lst, 0.75) - statistics.quantile(lst, 0.25)"))
        print("Spannweite:", cprint.yellow_bold_rounded(statistics.span(lst)), cprint.magenta("max(lst) - min(lst)"))
        print("Empirische Varianz:", cprint.yellow_bold_rounded(statistics.var(lst)),
              cprint.magenta("numpy.var(lst, ddof=1)"))
        print("Empirische Standardabweichung:", cprint.yellow_bold_rounded(statistics.std(lst)),
              cprint.magenta("math.sqrt(numpy.var(lst))"))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " Anderes Quantil ausrechnen\n" +
          cprint.bold(2) + " Funktion mit anderen Werten wiederholen\n" +
          cprint.bold(3) + " Funktionen zu beschreibender Statistik\n" +
          cprint.bold(4) + " Hauptmenü")

    match cinput.integer(1, 4):
        case 1:
            quantile()
            mean_median_mode_quartile_iqr_span_var_std(True)
        case 2:
            list1 = None
            list2 = None
            mean_median_mode_quartile_iqr_span_var_std()
        case 3:
            print("Werte beibehalten?\n" +
                  cprint.bold(1) + " Ja\n" +
                  cprint.bold(2) + " Nein")
            if cinput.integer(1, 2) == 2:
                list1 = None
                list2 = None
            functions_statistics()
        case 4:
            menu_main()


def quantile():
    if list1 is None:
        print("Liste für Quantil eingeben:")
        lst = input_list()
    else:
        lst = list1
    print("Anteil p als Dezimalzahl oder mit % eingeben:")
    p = cinput.float_fraction(True, False)
    print(cprint.rounded(p * 100) + "%-Quantil:", cprint.yellow_bold_rounded(statistics.quantile(lst, p)),
          cprint.magenta("numpy.quantile(lst, {}, method='averaged_inverted_cdf')".format(cprint.rounded(p))))


def corrcoef_covar():
    if list1 is None or list2 is None:
        print("1. Liste für empirischen Korrelationskoeffizienten und empirische Kovarianz eingeben:")
        lst1 = input_list()
        print("2. Liste für empirischen Korrelationskoeffizienten und empirische Kovarianz eingeben:")
        lst2 = input_list(False)
    else:
        lst1 = list1
        lst2 = list2
    print("Empirischer Korrelationskoeffizient:", cprint.yellow_bold_rounded(statistics.corrcoef(lst1, lst2)),
          cprint.magenta("statistics.pearsonr(lst1, lst2)[0]"))
    print("Empirische Kovarianz:", cprint.yellow_bold_rounded(statistics.covar(lst1, lst2)),
          cprint.magenta("statistics.covariance(lst1, lst2)"))


def det():
    if list1 is None or list2 is None:
        print("1. Liste für Bestimmtheitsmaß eingeben:")
        lst1 = input_list()
        print("2. Liste für Bestimmtheitsmaß eingeben:")
        lst2 = input_list(False)
    else:
        lst1 = list1
        lst2 = list2
    print("Bestimmtheitsmaß:", cprint.yellow_bold_rounded(statistics.det(lst1, lst2)),
          cprint.magenta("statistics.pearsonr(lst1, lst2)[0]**2"))


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
            print("Absolute Häufigkeiten:", cprint.yellow_bold(statistics.abs_frequency(lst, stringify=True)))
        case 2:
            print("Relative Häufigkeiten:", cprint.yellow_bold(statistics.rel_frequency(lst, stringify=True)))
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


def combination(elements_all=None, elements_sorted=None, elements_repetition=None):
    if elements_all is None:
        print("Werden alle Elemente angeordnet?\n" +
              cprint.bold(1) + " Ja\n" +
              cprint.bold(2) + " Nein")
        match cinput.integer(1, 2):
            case 1:
                elements_all = True
            case 2:
                elements_all = False

    if elements_sorted is None and not elements_all:
        print("Spielt die Reihenfolge eine Rolle?\n" +
              cprint.bold(1) + " Ja\n" +
              cprint.bold(2) + " Nein")
        match cinput.integer(1, 2):
            case 1:
                elements_sorted = True
            case 2:
                elements_sorted = False

    if elements_repetition is None and not elements_all:
        print("Sind Wiederholungen erlaubt?\n" +
              cprint.bold(1) + " Ja\n" +
              cprint.bold(2) + " Nein")
        match cinput.integer(1, 2):
            case 1:
                elements_repetition = True
            case 2:
                elements_repetition = False

    name = None
    if elements_all:
        name = "P(n, n)"
        print("Permutation ohne Wiederholung (z.B. CDs im Regal):", name)
        print("Anzahl der k-Permutationen aus einer Menge mit n Elementen ohne Wiederholungen")
    elif not elements_all and elements_sorted and not elements_repetition:
        name = "P(n, k)"
        print("Variation ohne Wiederholung (z.B. Podestplätze):", name)
        print("Anzahl der k-Permutationen aus einer Menge mit n Elementen ohne Wiederholungen")
    elif not elements_all and elements_sorted and elements_repetition:
        name = "P^W(n, k)"
        print("Variation mit Wiederholung (z.B. Passwörter):", name)
        print("Anzahl der k-Permutationen aus einer Menge mit n Elementen mit Wiederholungen")
    elif not elements_all and not elements_sorted and not elements_repetition:
        name = "C(n, k)"
        print("Kombination ohne Wiederholung (z.B. Lotto):", name)
        print("Anzahl der möglichen Kombinationen von k Elementen aus einer Menge mit n Elementen ohne Wiederholungen")
    elif not elements_all and not elements_sorted and elements_repetition:
        name = "C^W(n, k)"
        print("Kombination mit Wiederholung (z.B. Gummibärchen-Orakel):", name)
        print("Anzahl der möglichen Kombinationen von k Elementen aus einer Menge mit n Elementen mit Wiederholungen")

    print("\nGesamtmenge n eingeben:")
    n = cinput.integer(0, None)
    k = 0
    if not elements_all and elements_repetition:
        print("Auswahl k eingeben:")
        k = cinput.integer(0, None)
    elif not elements_all:
        print("Auswahl k eingeben:")
        k = cinput.integer(0, n)

    if elements_all:
        result = probability_discrete.p_n(n)
        print("P({}, {}) = {}! =".format(n, n, n), cprint.yellow_bold_rounded(result))
    elif not elements_all and elements_sorted and not elements_repetition:
        result = probability_discrete.p_n_k(n, k)
        print("P({}, {}) = {}! / ({}-{})! =".format(n, k, n, n, k), cprint.yellow_bold_rounded(result))
    elif not elements_all and elements_sorted and elements_repetition:
        result = probability_discrete.p_w(n, k)
        print("P^W({}, {}) = {}^{} =".format(n, k, n, k), cprint.yellow_bold_rounded(result))
    elif not elements_all and not elements_sorted and not elements_repetition:
        result = probability_discrete.c_n_k(n, k)
        print("C({}, {}) = ({} über {}) =".format(n, k, n, k), cprint.yellow_bold_rounded(result))
    elif not elements_all and not elements_sorted and elements_repetition:
        result = probability_discrete.c_w(n, k)
        print("C^W({}, {}) = (({}+{}-1) über {}) =".format(n, k, n, k, k), cprint.yellow_bold_rounded(result))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " {} mit anderen Werten berechnen\n".format(name) +
          cprint.bold(2) + " Kombinatorik-Formelsuche erneut starten\n" +
          cprint.bold(3) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(4) + " Hauptmenü")

    match cinput.integer(1, 4):
        case 1:
            combination(elements_all, elements_sorted, elements_repetition)
        case 2:
            combination()
        case 3:
            functions_probability_discrete()
        case 4:
            menu_main()


def laplace():
    print("Anzahl günstiger (benötigter) Fälle k eingeben:")
    k = cinput.integer(0, None)
    print("Anzahl möglicher Fälle n eingeben:")
    n = cinput.integer(1, None)

    print(cprint.bold("Laplace-Experiment:"))
    print("P(Ereignis) = {}/{} =".format(k, n), cprint.yellow_bold_rounded(probability_discrete.laplace(n, k)))


def discrete_random_variables(jump_to_options=False):
    global list1
    global list2

    if not jump_to_options:
        if list1 is None or list2 is None:
            print("Ereignisse eingeben:")
            lst1 = input_list()
            print("Zugehörige Wahrscheinlichkeit(en) als Bruch, Dezimalzahl oder in Prozent eingeben:")
            lst2 = input_probabilities(False, len(lst1))
        else:
            lst1 = list1
            lst2 = list2
        print("E(X) =", cprint.yellow_bold_rounded(probability_discrete.mean(lst1, lst2)))
        print("Var(X) =", cprint.yellow_bold_rounded(probability_discrete.var(lst1, lst2)))
        print("Std(X) =", cprint.yellow_bold_rounded(probability_discrete.std(lst1, lst2)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(genau x)\n" +
          cprint.bold(2) + " P(mindestens x)\n" +
          cprint.bold(3) + " P(höchstens x)\n" +
          cprint.bold(4) + " P(mehr als x)\n" +
          cprint.bold(5) + " P(weniger als x)\n" +
          cprint.bold(6) + " P(zwischen x und y)\n" +
          cprint.bold(7) + " Funktion erneut verwenden\n" +
          cprint.bold(8) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(9) + " Hauptmenü")
    match cinput.integer(1, 9):
        case 1:
            print("Anzahl erfolgreicher Versuche x für P(X = x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X = {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_discrete.pdf(list1, list2, x)))
            discrete_random_variables(True)
        case 2:
            print("Anzahl erfolgreicher Versuche x für P(X >= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X >= {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x - 1)),
                  cprint.yellow_bold_rounded(1 - probability_discrete.cdf(list1, list2, x - 1)))
            discrete_random_variables(True)
        case 3:
            print("Anzahl erfolgreicher Versuche x für P(X <= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X <= {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_discrete.cdf(list1, list2, x)))
            discrete_random_variables(True)
        case 4:
            print("Anzahl erfolgreicher Versuche x für P(X > x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X > {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(1 - probability_discrete.cdf(list1, list2, x)))
            discrete_random_variables(True)
        case 5:
            print("Anzahl erfolgreicher Versuche x für P(X < x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X < {}) = P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x - 1)),
                  cprint.yellow_bold_rounded(probability_discrete.cdf(list1, list2, x - 1)))
            discrete_random_variables(True)
        case 6:
            print("Anzahl erfolgreicher Versuche x für P(x <= X <= y) eingeben:")
            x = cinput.integer(0, None)
            print("Anzahl erfolgreicher Versuche y für P(x <= X <= y) eingeben:")
            y = cinput.integer(0, None)
            cdf_x = probability_discrete.cdf(list1, list2, x - 1)
            cdf_y = probability_discrete.cdf(list1, list2, y)
            print("P({} <= X <= {}) = P(X <= {}) - P(X <= {}) =".format(
                cprint.rounded(x), cprint.rounded(y), cprint.rounded(y), cprint.rounded(x - 1)),
                cprint.yellow_bold_rounded(cdf_y - cdf_x))
            discrete_random_variables(True)
        case 7:
            list1 = None
            list2 = None
            discrete_random_variables()
        case 8:
            list1 = None
            list2 = None
            functions_probability_discrete()
        case 9:
            menu_main()


def bernoulli_distributed(p=None):
    if p is None:
        print("Erfolgswahrscheinlichkeit p als Bruch, Dezimalzahl oder in Prozent eingeben:")
        p = cinput.float_fraction(True, True)
        print(cprint.bold("Bernoulli-Verteilung: X ~ Ber({})".format(cprint.rounded(p))))
        print("P(X = 0) =", cprint.yellow_bold_rounded(probability_discrete.bernoulli_pdf(p, 0)))
        print("P(X = 1) =", cprint.yellow_bold_rounded(probability_discrete.bernoulli_pdf(p, 1)))
        print("E(X) =", cprint.yellow_bold_rounded(probability_discrete.bernoulli_mean(p)))
        print("Var(X) =", cprint.yellow_bold_rounded(probability_discrete.bernoulli_var(p)))
        print("Std(X) =", cprint.yellow_bold_rounded(probability_discrete.bernoulli_std(p)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(genau x)\n" +
          cprint.bold(2) + " P(mindestens x)\n" +
          cprint.bold(3) + " P(höchstens x)\n" +
          cprint.bold(4) + " P(mehr als x)\n" +
          cprint.bold(5) + " P(weniger als x)\n" +
          cprint.bold(6) + " P(zwischen x und y)\n" +
          cprint.bold(7) + " Funktion erneut verwenden\n" +
          cprint.bold(8) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(9) + " Hauptmenü")

    match cinput.integer(1, 9):
        case 1:
            print("Anzahl erfolgreicher Versuche x für P(X = x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X = {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_discrete.bernoulli_pdf(p, x)))
            bernoulli_distributed(p)
        case 2:
            print("Anzahl erfolgreicher Versuche x für P(X >= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X >= {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x - 1)),
                  cprint.yellow_bold_rounded(1 - probability_discrete.bernoulli_cdf(p, x - 1)))
            bernoulli_distributed(p)
        case 3:
            print("Anzahl erfolgreicher Versuche x für P(X <= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X <= {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_discrete.bernoulli_cdf(p, x)))
            bernoulli_distributed(p)
        case 4:
            print("Anzahl erfolgreicher Versuche x für P(X > x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X > {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(1 - probability_discrete.bernoulli_cdf(p, x)))
            bernoulli_distributed(p)
        case 5:
            print("Anzahl erfolgreicher Versuche x für P(X < x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X < {}) = P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x - 1)),
                  cprint.yellow_bold_rounded(probability_discrete.bernoulli_cdf(p, x - 1)))
            bernoulli_distributed(p)
        case 6:
            print("Anzahl erfolgreicher Versuche x für P(x <= X <= y) eingeben:")
            x = cinput.integer(0, None)
            print("Anzahl erfolgreicher Versuche y für P(x <= X <= y) eingeben:")
            y = cinput.integer(0, None)
            cdf_x = probability_discrete.bernoulli_cdf(p, x - 1)
            cdf_y = probability_discrete.bernoulli_cdf(p, y)
            print("P({} <= X <= {}) = P(X <= {}) - P(X <= {}) =".format(
                cprint.rounded(x), cprint.rounded(y), cprint.rounded(y), cprint.rounded(x - 1)),
                cprint.yellow_bold_rounded(cdf_y - cdf_x))
            bernoulli_distributed(p)
        case 7:
            bernoulli_distributed()
        case 8:
            functions_probability_discrete()
        case 9:
            menu_main()


def geom_distributed(p=None):
    jump_to_options = p is not None

    if p is None:
        print("Wahrscheinlichkeit p als Bruch, Dezimalzahl oder in Prozent eingeben:")
        p = cinput.float_fraction(True, True)

    if not jump_to_options:
        print(cprint.bold("Geometrische Verteilung: X ~ geom({})".format(cprint.rounded(p))))
        print("E(X) =", cprint.yellow_bold_rounded(probability_discrete.geom_mean(p)))
        print("Var(X) =", cprint.yellow_bold_rounded(probability_discrete.geom_var(p)))
        print("Std(X) =", cprint.yellow_bold_rounded(probability_discrete.geom_std(p)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(genau x)\n" +
          cprint.bold(2) + " P(mindestens x)\n" +
          cprint.bold(3) + " P(höchstens x)\n" +
          cprint.bold(4) + " P(mehr als x)\n" +
          cprint.bold(5) + " P(weniger als x)\n" +
          cprint.bold(6) + " P(zwischen x und y)\n" +
          cprint.bold(7) + " Funktion erneut verwenden\n" +
          cprint.bold(8) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(9) + " Hauptmenü")

    match cinput.integer(1, 9):
        case 1:
            print("Anzahl erfolgreicher Versuche x für P(X = x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X = {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_discrete.geom_pdf(p, x)))
            geom_distributed(p)
        case 2:
            print("Anzahl erfolgreicher Versuche x für P(X >= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X >= {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x - 1)),
                  cprint.yellow_bold_rounded(1 - probability_discrete.geom_cdf(p, x - 1)))
            geom_distributed(p)
        case 3:
            print("Anzahl erfolgreicher Versuche x für P(X <= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X <= {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_discrete.geom_cdf(p, x)))
            geom_distributed(p)
        case 4:
            print("Anzahl erfolgreicher Versuche x für P(X > x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X > {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(1 - probability_discrete.geom_cdf(p, x)))
            geom_distributed(p)
        case 5:
            print("Anzahl erfolgreicher Versuche x für P(X < x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X < {}) = P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x - 1)),
                  cprint.yellow_bold_rounded(probability_discrete.geom_cdf(p, x - 1)))
            geom_distributed(p)
        case 6:
            print("Anzahl erfolgreicher Versuche x für P(x <= X <= y) eingeben:")
            x = cinput.integer(0, None)
            print("Anzahl erfolgreicher Versuche y für P(x <= X <= y) eingeben:")
            y = cinput.integer(0, None)
            cdf_x = probability_discrete.geom_cdf(p, x - 1)
            cdf_y = probability_discrete.geom_cdf(p, y)
            print("P({} <= X <= {}) = P(X <= {}) - P(X <= {}) =".format(
                cprint.rounded(x), cprint.rounded(y), cprint.rounded(y), cprint.rounded(x - 1)),
                cprint.yellow_bold_rounded(cdf_y - cdf_x))
            geom_distributed(p)
        case 7:
            geom_distributed()
        case 8:
            functions_probability_discrete()
        case 9:
            menu_main()


def binomial_distributed(n=None, p=None):
    jump_to_options = n is not None and p is not None

    if n is None:
        print("Anzahl Versuche n eingeben:")
        n = cinput.integer(0, None)
    if p is None:
        print("Wahrscheinlichkeit p als Bruch, Dezimalzahl oder in Prozent eingeben:")
        p = cinput.float_fraction(True, True)

    if not jump_to_options:
        print(cprint.bold("Binomialverteilung: X ~ Bin({}, {})".format(n, cprint.rounded(p))))
        print("E(X) =", cprint.yellow_bold_rounded(probability_discrete.binomial_mean(n, p)))
        print("Var(X) =", cprint.yellow_bold_rounded(probability_discrete.binomial_var(n, p)))
        print("Std(X) =", cprint.yellow_bold_rounded(probability_discrete.binomial_std(n, p)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + "  P(genau x)\n" +
          cprint.bold(2) + "  P(mindestens x)\n" +
          cprint.bold(3) + "  P(höchstens x)\n" +
          cprint.bold(4) + "  P(mehr als x)\n" +
          cprint.bold(5) + "  P(weniger als x)\n" +
          cprint.bold(6) + "  P(zwischen x und y)\n" +
          cprint.bold(7) + "  Verteilung anzeigen\n" +
          cprint.bold(8) + "  Funktion erneut verwenden\n" +
          cprint.bold(9) + "  Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(10) + " Hauptmenü")

    match cinput.integer(1, 10):
        case 1:
            print("Anzahl erfolgreicher Versuche x für P(X = x) eingeben:")
            x = cinput.integer(0, n)
            print("P(X = {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_discrete.binomial_pdf(n, p, x)))
            binomial_distributed(n, p)
        case 2:
            print("Anzahl erfolgreicher Versuche x für P(X >= x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X >= {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x - 1)),
                  cprint.yellow_bold_rounded(1 - probability_discrete.binomial_cdf(n, p, x - 1)))
            binomial_distributed(n, p)
        case 3:
            print("Anzahl erfolgreicher Versuche x für P(X <= x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X <= {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_discrete.binomial_cdf(n, p, x)))
            binomial_distributed(n, p)
        case 4:
            print("Anzahl erfolgreicher Versuche x für P(X > x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X > {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(1 - probability_discrete.binomial_cdf(n, p, x)))
            binomial_distributed(n, p)
        case 5:
            print("Anzahl erfolgreicher Versuche x für P(X < x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X < {}) = P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x - 1)),
                  cprint.yellow_bold_rounded(probability_discrete.binomial_cdf(n, p, x - 1)))
            binomial_distributed(n, p)
        case 6:
            print("Anzahl erfolgreicher Versuche x für P(x <= X <= y) eingeben:")
            x = cinput.integer(0, None)
            print("Anzahl erfolgreicher Versuche y für P(x <= X <= y) eingeben:")
            y = cinput.integer(0, None)
            cdf_x = probability_discrete.binomial_cdf(n, p, x - 1)
            cdf_y = probability_discrete.binomial_cdf(n, p, y)
            print("P({} <= X <= {}) = P(X <= {}) - P(X <= {}) =".format(
                cprint.rounded(x), cprint.rounded(y), cprint.rounded(y), cprint.rounded(x - 1)),
                cprint.yellow_bold_rounded(cdf_y - cdf_x))
            binomial_distributed(n, p)
        case 7:
            for t in range(0, n + 1):
                print("P(X = {}) =".format(t), cprint.yellow_bold_rounded(probability_discrete.binomial_pdf(n, p, t)))
            binomial_distributed(n, p)
        case 8:
            binomial_distributed()
        case 9:
            functions_probability_discrete()
        case 10:
            menu_main()


def poisson_distributed(lam=None):
    jump_to_options = lam is not None

    if lam is None:
        print("Durchschnittliche Auftrittsrate λ als Dezimalzahl eingeben:")
        lam = cinput.float_range(0, None)

    if not jump_to_options:
        print(cprint.bold("Poisson-Verteilung: X ~ Po({})".format(cprint.rounded(lam))))
        print("E(X) = λ =", cprint.yellow_bold_rounded(lam))
        print("Var(X) = λ =", cprint.yellow_bold_rounded(lam))
        print("Std(X) =", cprint.yellow_bold_rounded(probability_discrete.poisson_std(lam)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(genau x)\n" +
          cprint.bold(2) + " P(mindestens x)\n" +
          cprint.bold(3) + " P(höchstens x)\n" +
          cprint.bold(4) + " P(mehr als x)\n" +
          cprint.bold(5) + " P(weniger als x)\n" +
          cprint.bold(6) + " P(zwischen x und y)\n" +
          cprint.bold(7) + " Funktion erneut verwenden\n" +
          cprint.bold(8) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(9) + " Hauptmenü")

    match cinput.integer(1, 9):
        case 1:
            print("Anzahl erfolgreicher Versuche x für P(X = x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X = {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_discrete.poisson_pdf(lam, x)))
            poisson_distributed(lam)
        case 2:
            print("Anzahl erfolgreicher Versuche x für P(X >= x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X >= {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x - 1)),
                  cprint.yellow_bold_rounded(1 - probability_discrete.poisson_cdf(lam, x - 1)))
            poisson_distributed(lam)
        case 3:
            print("Anzahl erfolgreicher Versuche x für P(X <= x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X <= {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_discrete.poisson_cdf(lam, x)))
            poisson_distributed(lam)
        case 4:
            print("Anzahl erfolgreicher Versuche x für P(X > x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X > {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(1 - probability_discrete.poisson_cdf(lam, x)))
            poisson_distributed(lam)
        case 5:
            print("Anzahl erfolgreicher Versuche x für P(X < x) eingeben:")
            x = cinput.integer(0, None)
            print("P(X < {}) = P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x - 1)),
                  cprint.yellow_bold_rounded(probability_discrete.poisson_cdf(lam, x - 1)))
            poisson_distributed(lam)
        case 6:
            print("Anzahl erfolgreicher Versuche x für P(x <= X <= y) eingeben:")
            x = cinput.integer(0, None)
            print("Anzahl erfolgreicher Versuche y für P(x <= X <= y) eingeben:")
            y = cinput.integer(0, None)
            cdf_x = probability_discrete.poisson_cdf(lam, x - 1)
            cdf_y = probability_discrete.poisson_cdf(lam, y)
            print("P({} <= X <= {}) = P(X <= {}) - P(X <= {}) =".format(
                cprint.rounded(x), cprint.rounded(y), cprint.rounded(y), cprint.rounded(x - 1)),
                cprint.yellow_bold_rounded(cdf_y - cdf_x))
            poisson_distributed(lam)
        case 7:
            poisson_distributed()
        case 8:
            functions_probability_discrete()
        case 9:
            menu_main()


def probability_calculation():
    print(cprint.blue_bold("Kalkulationshilfe:\n") +
          cprint.bold(1) + " Mindestens x\n" +
          cprint.bold(2) + " Höchstens x\n" +
          cprint.bold(3) + " Mehr als x\n" +
          cprint.bold(4) + " Weniger als x\n" +
          cprint.bold(5) + " Zwischen x und y\n" +
          cprint.bold(6) + " x oder y\n" +
          cprint.bold(7) + " Bedingte Wahrscheinlichkeiten\n" +
          cprint.bold(8) + " Funktionen zu diskreter Wahrscheinlichkeitstheorie\n" +
          cprint.bold(9) + " Hauptmenü")

    match cinput.integer(1, 9):
        case 1:
            print("Anzahl erfolgreicher Versuche x für P(X >= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X >= {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold("1 - P(X <= {})".format(cprint.rounded(x - 1))))
        case 2:
            print("Anzahl erfolgreicher Versuche x für P(X <= x) eingeben:")
            x = cinput.float_range(0, None)
            print(cprint.yellow_bold("P(X <= {})".format(cprint.rounded(x))))
        case 3:
            print("Anzahl erfolgreicher Versuche x für P(X > x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X > {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold("1 - P(X <= {})".format(cprint.rounded(x))))
        case 4:
            print("Anzahl erfolgreicher Versuche x für P(X < x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X < {}) =".format(cprint.rounded(x)),
                  cprint.yellow_bold("P(X <= {})".format(cprint.rounded(x - 1))))
        case 5:
            print("Anzahl erfolgreicher Versuche x für P(x <= X <= y) eingeben:")
            x = cinput.float_range(0, None)
            print("Anzahl erfolgreicher Versuche y für P(x <= X <= y) eingeben:")
            y = cinput.float_range(0, None)
            print("P({} <= X <= {}) =".format(cprint.rounded(x), cprint.rounded(y)),
                  cprint.yellow_bold("P(X <= {}) - P(X <= {})".format(cprint.rounded(y), cprint.rounded(x - 1))))
        case 6:
            print("Anzahl erfolgreicher Versuche x für P(X = x ∨ X = y) eingeben:")
            x = cinput.float_range(0, None)
            print("Anzahl erfolgreicher Versuche y für P(X = x ∨ X = y) eingeben:")
            y = cinput.float_range(0, None)
            print("P(X = {} ∨ X = {}) =".format(cprint.rounded(x), cprint.rounded(y)),
                  cprint.yellow_bold("P(X = {}) + P(X = {})".format(cprint.rounded(x), cprint.rounded(y))))
        case 7:
            print("Bezeichnung der gesuchten Wahrscheinlichkeit eingeben:")
            probability = cinput.string()
            print("Bezeichnung der Bedingung eingeben:")
            condition = cinput.string()
            top = "P({}) * P({}|{})".format(probability, condition, probability)
            bottom = "P({}) * P({}|{}) + P(^{}) * P({}|^{})".format(
                probability, condition, probability, probability, condition, probability
            )
            print("P({}|{}) =".format(probability, condition),
                  cprint.yellow_bold("({})".format(top)), cprint.bold("/"),
                  cprint.yellow_bold("P({})".format(condition)), "=", cprint.yellow("({})".format(top)), "/",
                  cprint.yellow("({})".format(bottom)))
        case 8:
            functions_probability_discrete()
        case 9:
            menu_main()


def uniform_distributed(a=None, b=None):
    jump_to_options = a is not None and b is not None

    if a is None:
        print("Minimalen Wert a eingeben:")
        a = cinput.float_fraction()
    if b is None:
        print("Maximalen Wert b eingeben:")
        b = cinput.float_fraction()

    if not jump_to_options:
        print(cprint.bold("Gleichverteilung: X ~ U({}, {})".format(cprint.rounded(a), cprint.rounded(b))))
        print("E(X) =", cprint.yellow_bold_rounded(probability_continuous.uniform_mean(a, b)))
        print("Var(X) =", cprint.yellow_bold_rounded(probability_continuous.uniform_var(a, b)))
        print("Std(X) =", cprint.yellow_bold_rounded(probability_continuous.uniform_std(a, b)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(mindestens/mehr als x)\n" +
          cprint.bold(2) + " P(höchstens/weniger als x)\n" +
          cprint.bold(3) + " P(zwischen x und y)\n" +
          cprint.bold(4) + " Quantil berechnen\n" +
          cprint.bold(5) + " Funktion erneut verwenden\n" +
          cprint.bold(6) + " Funktionen zu kontinuierlicher Wahrscheinlichkeitstheorie\n" +
          cprint.bold(7) + " Hauptmenü")

    match cinput.integer(1, 7):
        case 1:
            print("Anzahl erfolgreicher Versuche x für P(X >= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X >= {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(1 - probability_continuous.uniform_cdf(a, b, x)))
            normal_distributed(a, b)
        case 2:
            print("Anzahl erfolgreicher Versuche x für P(X <= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_continuous.uniform_cdf(a, b, x)))
            uniform_distributed(a, b)
        case 3:
            print("Anzahl erfolgreicher Versuche x für P(x <= X <= y) eingeben:")
            x = cinput.float_range(0, None)
            print("Anzahl erfolgreicher Versuche y für P(x <= X <= y) eingeben:")
            y = cinput.float_range(0, None)
            cdf_x = probability_continuous.uniform_cdf(a, b, x)
            cdf_y = probability_continuous.uniform_cdf(a, b, y)
            print("P({} <= X <= {}) = P(X <= {}) - P(X <= {}) =".format(
                cprint.rounded(x), cprint.rounded(y), cprint.rounded(y), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(cdf_y - cdf_x))
            uniform_distributed(a, b)
        case 4:
            print("Anteil p als Dezimalzahl oder mit % eingeben:")
            p = cinput.float_fraction(True, False)
            print(cprint.rounded(p * 100) + "%-Quantil:",
                  cprint.yellow_bold_rounded(probability_continuous.uniform_ppf(a, b, p)))
            uniform_distributed(a, b)
        case 5:
            uniform_distributed()
        case 6:
            functions_probability_continuous()
        case 7:
            menu_main()


def exponential_distributed(lam=None):
    jump_to_options = lam is not None

    if lam is None:
        print("Durchschnittliche Auftrittsrate λ als Dezimalzahl eingeben:")
        lam = cinput.float_range(0, None)

    if not jump_to_options:
        print(cprint.bold("Exponentialverteilung: X ~ exp({})".format(cprint.rounded(lam))))
        print("E(X) =", cprint.yellow_bold_rounded(probability_continuous.exponential_mean(lam)))
        print("Var(X) =", cprint.yellow_bold_rounded(probability_continuous.exponential_var(lam)))
        print("Std(X) =", cprint.yellow_bold_rounded(probability_continuous.exponential_std(lam)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(mindestens/mehr als x)\n" +
          cprint.bold(2) + " P(höchstens/weniger als x)\n" +
          cprint.bold(3) + " P(zwischen x und y)\n" +
          cprint.bold(4) + " Quantil berechnen\n" +
          cprint.bold(5) + " Funktion erneut verwenden\n" +
          cprint.bold(6) + " Funktionen zu kontinuierlicher Wahrscheinlichkeitstheorie\n" +
          cprint.bold(7) + " Hauptmenü")

    match cinput.integer(1, 7):
        case 1:
            print("Anzahl erfolgreicher Versuche x für P(X >= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X >= {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(1 - probability_continuous.exponential_cdf(lam, x)))
            exponential_distributed(lam)
        case 2:
            print("Anzahl erfolgreicher Versuche x für P(X <= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_continuous.exponential_cdf(lam, x)))
            exponential_distributed(lam)
        case 3:
            print("Anzahl erfolgreicher Versuche x für P(x <= X <= y) eingeben:")
            x = cinput.float_range(0, None)
            print("Anzahl erfolgreicher Versuche y für P(x <= X <= y) eingeben:")
            y = cinput.float_range(0, None)
            cdf_x = probability_continuous.exponential_cdf(lam, x)
            cdf_y = probability_continuous.exponential_cdf(lam, y)
            print("P({} <= X <= {}) = P(X <= {}) - P(X <= {}) =".format(
                cprint.rounded(x), cprint.rounded(y), cprint.rounded(y), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(cdf_y - cdf_x))
            exponential_distributed(lam)
        case 4:
            print("Anteil p als Dezimalzahl oder mit % eingeben:")
            p = cinput.float_fraction(True, False)
            print(cprint.rounded(p * 100) + "%-Quantil:",
                  cprint.yellow_bold_rounded(probability_continuous.exponential_ppf(lam, p)))
            exponential_distributed(lam)
        case 5:
            exponential_distributed()
        case 6:
            functions_probability_continuous()
        case 7:
            menu_main()


def normal_distributed(mu=None, sigma=None):
    jump_to_options = mu is not None and sigma is not None

    if mu is None:
        print("Erwartungswert μ als Dezimalzahl eingeben (Standardnormalverteilung = 0):")
        mu = cinput.float_fraction(False, False)

    if sigma is None:
        print("Standardabweichung σ als Dezimalzahl eingeben (Standardnormalverteilung = 1):")
        sigma = cinput.float_fraction(False, False)

    if not jump_to_options:
        print(cprint.bold("Normalverteilung: X ~ N({}, {})".format(cprint.rounded(mu), cprint.rounded(sigma))))
        print("E(X) =", cprint.yellow_bold_rounded(probability_continuous.normal_mean(mu)))
        print("Var(X) =", cprint.yellow_bold_rounded(probability_continuous.normal_var(sigma)))
        print("Std(X) =", cprint.yellow_bold_rounded(probability_continuous.normal_std(sigma)))

    print(cprint.blue_bold("\nOptionen:\n") +
          cprint.bold(1) + " P(mindestens/mehr als x)\n" +
          cprint.bold(2) + " P(höchstens/weniger als x)\n" +
          cprint.bold(3) + " P(zwischen x und y)\n" +
          cprint.bold(4) + " Quantil berechnen\n" +
          cprint.bold(5) + " Funktion erneut verwenden\n" +
          cprint.bold(6) + " Funktionen zu kontinuierlicher Wahrscheinlichkeitstheorie\n" +
          cprint.bold(7) + " Hauptmenü")

    match cinput.integer(1, 7):
        case 1:
            print("Anzahl erfolgreicher Versuche x für P(X >= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X >= {}) = 1 - P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(1 - probability_continuous.normal_cdf(mu, sigma, x)))
            normal_distributed(mu, sigma)
        case 2:
            print("Anzahl erfolgreicher Versuche x für P(X <= x) eingeben:")
            x = cinput.float_range(0, None)
            print("P(X <= {}) =".format(cprint.rounded(x), cprint.rounded(x)),
                  cprint.yellow_bold_rounded(probability_continuous.normal_cdf(mu, sigma, x)))
            normal_distributed(mu, sigma)
        case 3:
            print("Anzahl erfolgreicher Versuche x für P(x <= X <= y) eingeben:")
            x = cinput.float_range(0, None)
            print("Anzahl erfolgreicher Versuche y für P(x <= X <= y) eingeben:")
            y = cinput.float_range(0, None)
            cdf_x = probability_continuous.normal_cdf(mu, sigma, x)
            cdf_y = probability_continuous.normal_cdf(mu, sigma, y)
            print("P({} <= X <= {}) = P(X <= {}) - P(X <= {}) =".format(
                cprint.rounded(x), cprint.rounded(y), cprint.rounded(y), cprint.rounded(x)),
                cprint.yellow_bold_rounded(cdf_y - cdf_x))
            normal_distributed(mu, sigma)
        case 4:
            print("Anteil p als Dezimalzahl oder mit % eingeben:")
            p = cinput.float_fraction(True, False)
            print(cprint.rounded(p * 100) + "%-Quantil:",
                  cprint.yellow_bold_rounded(probability_continuous.normal_ppf(mu, sigma, p)))
            normal_distributed(mu, sigma)
        case 5:
            normal_distributed()
        case 6:
            functions_probability_continuous()
        case 7:
            menu_main()


def menu_main():
    global list1
    global list2
    list1 = None  # reset statistic lists
    list2 = None

    print(cprint.blue_bold("Hauptmenü:\n") +
          cprint.bold(1) + " Beschreibende Statistik\n" +
          cprint.bold(2) + " Diskrete Wahrscheinlichkeitstheorie\n" +
          cprint.bold(3) + " Kontinuierliche Wahrscheinlichkeitstheorie")

    match cinput.integer(1, 3):
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
              cprint.bold(2) + " Laplace-Experiment (alle Ausgänge mit identischer Wahrscheinlichkeit)\n" +
              cprint.bold(3) + " Zufallsvariablen\n" +
              cprint.bold(4) + " Bernoulli-Verteilung (genau zwei mögliche Ausgänge)\n" +
              cprint.bold(5) + " Geometrische Verteilung (Wartezeit bis zum ersten Erfolg)\n" +
              cprint.bold(6) + " Binomialverteilung (Anzahl Erfolge)\n" +
              cprint.bold(7) + " Poisson-Verteilung (Auftrittsrate über Zeitraum betrachtet)\n" +
              cprint.bold(8) + " Kalkulationshilfe\n" +
              cprint.bold(9) + " Hauptmenü")
        func_code = cinput.integer(1, 9)

    match func_code:
        case 1:
            combination()
        case 2:
            laplace()
        case 3:
            discrete_random_variables()
        case 4:
            bernoulli_distributed()
        case 5:
            geom_distributed()
        case 6:
            binomial_distributed()
        case 7:
            poisson_distributed()
        case 8:
            probability_calculation()
        case 9:
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
              cprint.bold(1) + " Gleichverteilung (bei gleichmäßiger/unbekannter Verteilung)\n" +
              cprint.bold(2) + " Exponentialverteilung (Dauer zufälliger Zeitintervalle)\n" +
              cprint.bold(3) + " Normalverteilung (natürliche/technische Phänomene)\n" +
              cprint.bold(4) + " Hauptmenü")
        func_code = cinput.integer(1, 4)

    match func_code:
        case 1:
            uniform_distributed()
        case 2:
            exponential_distributed()
        case 3:
            normal_distributed()
        case 4:
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


print("Exam Helper v1.3.2")
print(cprint.yellow("Viel Erfolg!\n"))
menu_main()
