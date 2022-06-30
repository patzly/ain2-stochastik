from utils import print_util as cprint


def invalid(msg=None):
    if msg is None:
        print(cprint.red("Ungültige Eingabe. Erneut versuchen:"))
    else:
        print(cprint.red("Ungültige Eingabe ({}). Erneut versuchen:".format(msg)))


def rounded(n):
    result = round(n, 3)
    if result % 1 == 0:
        return int(result)
    else:
        return float(result)


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
        invalid()
        return integer(mini, maxi)

    if mini is not None and maxi is not None:
        if mini <= user <= maxi:
            return user
        else:
            invalid()
            return integer(mini, maxi)
    elif mini is not None and maxi is None:
        if user >= mini:
            return user
        else:
            invalid()
            return integer(mini, maxi)
    elif mini is None and maxi is not None:
        if user <= maxi:
            return user
        else:
            invalid()
            return integer(mini, maxi)
    else:
        return user


def percentage(allow_fraction=True):
    # Prevent ValueError from being thrown when input is not a float or not in 0%-100% bounds
    user = string()
    try:
        if allow_fraction and "/" in user:
            operators = user.split("/")
            if len(operators) == 2:
                result = float(float(operators[0].strip()) / float(operators[1].strip()))
            else:
                invalid()
                return percentage()
        else:
            result = float(user)

        if 0 <= result <= 1:
            return rounded(result)
        else:
            invalid()
            return percentage()
    except ValueError:
        invalid()
        return percentage()


def float_above_zero():
    # Prevent ValueError from being thrown when input is not a float or <= 0
    try:
        result = float(string())
        if result > 0:
            return rounded(result)
        else:
            invalid("Werte kleiner gleich 0 unzulässig")
            return float_above_zero()
    except ValueError:
        invalid("nur Dezimalzahlen zulässig")
        return float_above_zero()
