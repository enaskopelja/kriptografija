import numpy as np
from commons import yield_in_ns, reverse_lookup, _print_matrix

plaintext = "VERNAM"
cypher = "DUCTKY"
m = 2


def _construct_matrices():
    x = np.empty((m, m))
    y = np.empty((m, m))
    for i, row_plain, row_cypher in zip(range(m), yield_in_ns(plaintext, m), yield_in_ns(cypher, m)):
        x[i:i + m] = [reverse_lookup(letter) for letter in row_plain]
        y[i:i + m] = [reverse_lookup(letter) for letter in row_cypher]

    return x, y


def _invert_2x2(x):
    detx = np.linalg.det(x) % 26
    inv_mod26 = pow(int(np.round(detx)), -1, 26)

    identity_2x2 = np.identity(2)
    multiplier = identity_2x2 + (identity_2x2 - 1)

    return ((np.flip(np.flip(x, 0), 1) * multiplier).T * inv_mod26) % 26


def _to_ndarray(text):
    return np.array([reverse_lookup(x) for x in text])


def _check(key):
    for pair_plain, pair_cypher in zip(yield_in_ns(plaintext, 2), yield_in_ns(cypher, 2)):
        assert (_to_ndarray(pair_cypher) == ((_to_ndarray(pair_plain) @ key) % 26).astype('int')).all()


def main():
    x, y = _construct_matrices()
    _print_matrix(x, "X")
    _print_matrix(y, "e(X)")

    xinv = _invert_2x2(x)
    _print_matrix(xinv, "X^-1")

    key = (xinv @ y) % 26
    _print_matrix(key, "K")

    _check(key)


if __name__ == '__main__':
    main()
