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

from utils import print_util as cprint


def invalid(msg=None):
    if msg is None:
        print(cprint.red("Ungültige Eingabe. Erneut versuchen:"))
    else:
        print(cprint.red("{}. Erneut versuchen:".format(msg)))


def string():
    # Prevent KeyboardInterrupt from being thrown when program is stopped
    try:
        return input().strip()
    except (KeyboardInterrupt, EOFError):
        raise SystemExit(0)


def integer(mini=None, maxi=None):
    # Prevent ValueError from being thrown when input is not a number or not in min max bounds
    try:
        user = int(string())
    except ValueError:
        invalid("Nur ganze Zahlen zulässig")
        return integer(mini, maxi)

    if mini is not None and maxi is not None:
        if mini <= user <= maxi:
            return user
        else:
            invalid("Nur Werte von {} bis {} zulässig".format(mini, maxi))
            return integer(mini, maxi)
    elif mini is not None and maxi is None:
        if user >= mini:
            return user
        else:
            invalid("Nur Werte ab {} zulässig".format(mini))
            return integer(mini, maxi)
    elif mini is None and maxi is not None:
        if user <= maxi:
            return user
        else:
            invalid("Nur Werte bis {} zulässig".format(maxi))
            return integer(mini, maxi)
    else:
        return user


def float_fraction(percent_bounds=False, allow_fraction=False):
    # Prevent ValueError from being thrown when input is not a float or not in bounds
    user = string()
    try:
        if allow_fraction and "/" in user and "%" not in user:
            operators = user.split("/")
            if len(operators) == 2:
                result = float(float(operators[0].strip()) / float(operators[1].strip()))
            else:
                invalid("Nur einmalige Division zulässig")
                return float_fraction(percent_bounds, allow_fraction)
        elif percent_bounds and "%" in user and "/" not in user:
            pct = user.replace("%", "").strip()
            result = float(pct) / 100
        else:
            result = float(user)

        if percent_bounds and (result < 0 or result > 1):
            invalid("Nur Werte von 0 bis 1 zulässig")
            return float_fraction(percent_bounds, allow_fraction)
        else:
            return float(result)
    except ValueError:
        if allow_fraction:
            invalid("Nur Dezimalzahlen und Brüche zulässig")
        else:
            invalid("Nur Dezimalzahlen zulässig")
        return float_fraction(percent_bounds, allow_fraction)


def floats_fraction(percent_bounds=False, allow_fraction=False):
    # Prevent ValueError from being thrown when input is not a float or not in bounds
    user = string().split(" ")
    floats = [.0] * len(user)
    for i in range(len(user)):
        try:
            if allow_fraction and "/" in user[i] and "%" not in user[i]:
                operators = user[i].split("/")
                if len(operators) == 2:
                    result = float(float(operators[0].strip()) / float(operators[1].strip()))
                else:
                    invalid("Nur einmalige Division zulässig")
                    return floats_fraction(percent_bounds, allow_fraction)
            elif percent_bounds and "%" in user[i] and "/" not in user[i]:
                pct = user[i].replace("%", "").strip()
                result = float(pct) / 100
            else:
                result = float(user[i])
            if percent_bounds and (result < 0 or result > 1):
                invalid("Nur Werte von 0 bis 1 zulässig")
                return floats_fraction(percent_bounds, allow_fraction)
            else:
                floats[i] = float(result)
        except TypeError:
            if allow_fraction:
                invalid("Nur Dezimalzahlen und Brüche zulässig")
            else:
                invalid("Nur Dezimalzahlen zulässig")
            return floats_fraction(percent_bounds, allow_fraction)
    return floats


def float_range(mini=None, maxi=None):
    # Prevent ValueError from being thrown when input is not a number or not in min max bounds
    try:
        user = float(string())
    except ValueError:
        invalid("Nur Dezimalzahlen zulässig")
        return float_range(mini, maxi)

    if mini is not None and maxi is not None:
        if mini <= user <= maxi:
            return user
        else:
            invalid("Nur Werte von {} bis {} zulässig".format(mini, maxi))
            return float_range(mini, maxi)
    elif mini is not None and maxi is None:
        if user >= mini:
            return user
        else:
            invalid("Nur Werte ab {} zulässig".format(mini))
            return float_range(mini, maxi)
    elif mini is None and maxi is not None:
        if user <= maxi:
            return user
        else:
            invalid("Nur Werte bis {} zulässig".format(maxi))
            return float_range(mini, maxi)
    else:
        return user
