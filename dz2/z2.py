import string
from functools import partial

from commons import yield_in_ns, _print_matrix

plaintext = 'FRIEDMAN'
key = 'CRYPTOGRAPHY'


def _uniq(text):
    seen = set()
    return [x for x in text if not (x in seen or seen.add(x))]


def _get_rest(uniq_key):
    a = set(string.ascii_uppercase)
    a.remove("W")
    yield from sorted(a - set(uniq_key))


def _create_matrix():
    uniq_key = _uniq(key)
    uniq_len = len(uniq_key)
    rest = _get_rest(uniq_key)

    matrix = [uniq_key[i:i + 5] for i in range(uniq_len // 5)]
    matrix.append(
        uniq_key[-(uniq_len % 5 + 1):] + [l for l, _ in zip(rest, range(5 - uniq_len % 5 - 1))]
    )

    matrix.extend(five for five in yield_in_ns(rest, 5))

    _print_matrix(matrix, header="Matrica")

    return matrix


def _find_in_matrix(matrix, letter):
    for i, row in enumerate(matrix):
        try:
            j = row.index(letter)
            return i, j
        except ValueError:
            continue


def encrypt(matrix):
    for bigram in yield_in_ns(plaintext, 2):
        (i1, j1), (i2, j2) = map(partial(_find_in_matrix, matrix), bigram)
        if i1 == i2:
            yield matrix[i1][(j1 + 1) % 5] + matrix[i1][(j2 + 1) % 5]
        elif j1 == j2:
            yield matrix[(i1 + 1) % 5][j1] + matrix[(i2 + 1) % 5][j1]
        else:
            yield matrix[i1][j2] + matrix[i2][j1]


def main():
    matrix = _create_matrix()
    print("Sifrat:", ''.join(encrypt(matrix)))


if __name__ == '__main__':
    main()
