from utils import statistics_util as stats
from utils import probability_discrete_util as probs
from utils import print_util as cprint
import hashlib
import string
import time


def task_1_11():
    attraction = [7, 4, 10, 10, 9, 3, 9, 6]
    salary = [65, 60, 40, 70, 45, 40, 65, 55]
    interesting = [3, 10, 9, 1, 5, 10, 2, 3]
    cprint.magenta('Aufgabe 1.11: Jobsuche')
    cprint.cyan('Teilaufgabe 1.11.1')
    print('Modalwert:', stats.mode(attraction))
    print('Arithmetisches Mittel:', stats.mean(attraction))
    print('Empirische Standardabweichung:', stats.std(attraction))
    print('25%-Quartil:', stats.quantile(attraction, 0.25))
    print('50%-Quartil:', stats.quantile(attraction, 0.50))
    print('75%-Quartil:', stats.quantile(attraction, 0.75))
    print('60%-Quantil:', stats.quantile(attraction, 0.60))
    cprint.cyan('Teilaufgabe 1.11.2')
    print('rA,G:', stats.corrcoef(attraction, salary))
    print('rA,I:', stats.corrcoef(attraction, interesting))
    print('rG,I:', stats.corrcoef(salary, interesting))
    print()


def task_2_1():
    cprint.magenta('Aufgabe 2.1: Würfeln mit einem W10')
    print()


def task_2_3():
    cprint.magenta('Aufgabe 2.3: PINs')
    cprint.cyan('Teilaufgabe 2.3.1')
    print('Jede Ziffer mehrfach')
    print('Jede Ziffer mehrfach, erste Stelle keine Null')
    cprint.cyan('Teilaufgabe 2.3.2')
    print('Jede Ziffer mehrfach')
    print('Jede Ziffer mehrfach, erste Stelle keine Null')
    print()


def task_2_4():
    cprint.magenta('Aufgabe 2.4: Sockenschublade')
    print('Zwei rote')
    print('Zwei blaue')
    print('Zwei verschiedene')
    print('Zwei gleiche')
    print()


def task_2_7():
    cprint.magenta('Aufgabe 2.7: Zeitungsleser')
    print('Beide Lokalblätter')
    print('Kein Lokalblatt')
    print('Genau ein Lokalblatt')
    print()


def task_2_12():
    cprint.magenta('Aufgabe 2.12: Passwortknacken')
    print('Anzahl Möglichkeiten:', probs.factorial_rpt(62, 5))
    duration = 1115  # find_pw()
    print('Passwort: S0nN3')
    print('Laufzeit: {} Minuten'.format(round(duration/60, 1)))
    print()


def find_pw():
    sha1 = '39228d06a988045c5caaa97bf0a6158893d51862'
    chars = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    possibilities = len(chars)**5
    attempts = 0
    start = time.time()
    for z in chars:
        duration = int(time.time() - start)
        print('{} attempts remaining, elapsed time: {} seconds'.format(possibilities - attempts, duration))
        for y in chars:
            for x in chars:
                for w in chars:
                    for v in chars:
                        attempts += 1
                        pw = v + w + x + y + z
                        sha = hashlib.sha1(pw.encode('UTF-8'), usedforsecurity=False).hexdigest()
                        if sha == sha1:
                            duration = int(time.time() - start)
                            print('Password: {}'.format(pw))
                            # 'S0nN3' after 18,6 minutes
                            return duration
    cprint.red('No password found for this hash sum!')
    return int(time.time() - start)


task_1_11()
task_2_1()
task_2_3()
task_2_4()
task_2_7()
task_2_12()
