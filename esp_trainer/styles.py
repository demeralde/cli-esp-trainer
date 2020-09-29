from typing import Callable

from art import tprint
from colorama import Fore


def _print_pretty_text(text: str, font: str):
    tprint(text, font)

def _print_coloured_text(colour: str, text: str, font: str):
    print(Fore.LIGHTMAGENTA_EX, end="")
    _print_pretty_text(text, font)
    print(Fore.RESET)

def print_title(text: str):
    _print_coloured_text(Fore.LIGHTMAGENTA_EX, text, "future_8")

def print_text(text: str):
    _print_pretty_text(text, "lilia")
