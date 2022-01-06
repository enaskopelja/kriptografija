from typing import TypeVar, Union

import numpy as np

StrPolynomial = TypeVar('StrPolynomial', bound=str)
HexPolynomial = TypeVar('HexPolynomial', bound=str)


def _pretty_monomial(exp):
    if exp == 0:
        return "1"
    if exp == 1:
        return "x"
    return f"x^{exp}"


def pretty(polynomial):
    return " + ".join(_pretty_monomial(exp) for exp, coef in enumerate(reversed(polynomial)) if coef)


def _exponents(terms):
    for term in terms:
        if "x" in term:
            _, exp = term.split("x")
            exp = exp.strip()
            yield int(exp.replace("^", "").strip()) if exp else 1
        else:
            yield 0


def _str_to_numpy(poly_str: StrPolynomial):
    terms = poly_str.strip().split("+")
    exponents = list(_exponents(terms))

    res = np.zeros((max(exponents) + 1,))
    res[exponents] = 1

    return np.flip(res, 0)


def _hex_to_numpy(poly_str: HexPolynomial):
    return list(map(int, list(bin(int(poly_str, 16))[2:])))


def multiply(
        poly1: Union[HexPolynomial, StrPolynomial],
        poly2: Union[HexPolynomial, StrPolynomial],
        poly_type='str',
        verbose=False,
):
    poly1, poly2 = map(_hex_to_numpy if poly_type == 'hex' else _str_to_numpy, [poly1, poly2])

    res = np.polymul(poly1, poly2)
    res %= 2

    if verbose:
        print(pretty(res))

    _, res = np.polydiv(res, np.array([1, 0, 0, 0, 1, 1, 0, 1, 1]))
    return res.astype('int') % 2


def main(poly1: StrPolynomial, poly2: StrPolynomial, verbose=False):
    return multiply(poly1, poly2, verbose=verbose)


def _test():
    assert pretty(multiply("   1+x+ x^ 2+ x ^4+ x^6", "x7+x+1")) == pretty(multiply("57", "83", 'hex'))
    assert pretty(multiply("57", "83", 'hex')) == "1 + x^6 + x^7"


if __name__ == '__main__':
    _test()
    print(pretty(main("x7 + x6 + x5 + x3 + x + 1", "x6 + x4 + x + 1", verbose=True)))
