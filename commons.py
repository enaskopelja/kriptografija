import string
from collections import Counter
from typing import Iterable, List

cro_freqs = {
    "A": 0.115,
    "B": 0.015,
    "C": 0.028,
    "D": 0.037,
    "E": 0.084,
    "F": 0.003,
    "G": 0.016,
    "H": 0.008,
    "I": 0.098,
    "J": 0.051,
    "K": 0.036,
    "L": 0.033,
    "M": 0.031,
    "N": 0.066,
    "O": 0.090,
    "P": 0.029,
    "Q": 0,
    "R": 0.054,
    "S": 0.056,
    "T": 0.048,
    "U": 0.043,
    "V": 0.035,
    "W": 0,
    "X": 0,
    "Y": 0,
    "Z": 0.023,
}

DIVIDER = '---------------------------'


def reverse_lookup(letter: str) -> int:
    return ord(letter.upper()) - ord('A')


def lookup(n: int) -> str:
    return string.ascii_uppercase[n]


def n_grams(text, n) -> List:
    return [text[i:i + n] for i in range(len(text) - n + 1)]


def count_n_grams(cypher: str, n: int = 2) -> Counter:
    return Counter(n_grams(cypher, n))


def yield_in_ns(x: Iterable, n: int) -> List:
    curr = []
    for i, x in enumerate(x):
        if not i % n and i > 0:
            yield curr
            curr = []

        curr.append(x)
    yield curr


def _print_matrix(matrix, header=None):
    print()
    if header:
        print(header)
    print(DIVIDER)
    for row in matrix:
        print(*row)


def is_consonant(letter):
    return letter.upper() not in "AEIOU"


MOST_COMMON_CRO_BIGRAMS = """
AK, AN, AS, AT, AV, CI, DA, ED, EN, IC, IJ, IN,
IS, JA, JE, KA, KO, LI, NA, NE, NI, NO, OD, OJ,
OS, OV, PO, PR, RA, RE, RI, ST, TA, TI, VA, ZA
""".strip().replace(',', '').replace('\n', ' ').split(" ")
