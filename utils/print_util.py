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
