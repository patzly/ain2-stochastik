class Colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def magenta(text):
    return Colors.MAGENTA + str(text) + Colors.END


def blue(text):
    return Colors.BLUE + str(text) + Colors.END


def blue_bold(text):
    return bold(blue(text))


def cyan(text):
    return Colors.CYAN + str(text) + Colors.END


def green(text):
    return Colors.GREEN + str(text) + Colors.END


def yellow(text):
    return Colors.YELLOW + str(text) + Colors.END


def yellow_bold(text):
    return bold(yellow(text))


def red(text):
    return Colors.RED + str(text) + Colors.END


def bold(text):
    return Colors.BOLD + str(text) + Colors.END


def underline(text):
    return Colors.UNDERLINE + str(text) + Colors.END
