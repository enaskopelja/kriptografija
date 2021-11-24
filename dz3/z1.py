import itertools
import math

import numpy as np

from commons import is_consonant, MOST_COMMON_CRO_BIGRAMS, _print_matrix, DIVIDER

# SIFRAT = """
# AAOSA JRTIE EAAAU SCEAE IANPI JAJJN FVSOI RZVPH NIONA RNZIJ INUSS NTRZU TIC
# """.replace(" ", "").replace('\n', "")


SIFRAT = """
ITTUJ PSTAL NATCN RIUSK ENJIK EIMAD
KOATU RAANI ITIAO VPSAL MAEJI CMARA
PRSVO COOLS JKECR
""".replace(" ", "").replace('\n', "")


def _calc_prime_factors(n):
    i = 2
    upper_bound = math.floor(math.sqrt(n))
    while i <= upper_bound:
        if n % i == 0:
            n //= i
            yield i
        else:
            i += 1


def _two_partition(multiset):
    yield from {
        (tuple(sorted(p[:i])), tuple(sorted(p[i:]))) for p in itertools.permutations(multiset) for i in
        range(1, len(multiset))
    }


def _calc_row_col(candidates, *, col_lb, col_ub):
    assert col_lb < col_ub
    for row, col in _two_partition(candidates):
        row, col = math.prod(row), math.prod(col)

        if col_lb < col < col_ub:
            yield row, col


def _print_matrix_with_ratios(matrix, header=None):
    print()
    if header:
        print(header)
    print(DIVIDER)
    row, col = matrix.shape
    for r in matrix:
        consonants = sum(is_consonant(rr) for rr in r)
        print(*r, f" {1 - consonants / col:.2f}:{consonants / col:.2f}")


def _construct_matrix(row, col):
    matrix = np.zeros((row, col), dtype='str')
    for r in range(row):
        matrix[r, :] = list(SIFRAT[r::row])

    _print_matrix_with_ratios(matrix, header=matrix.shape)
    consonants = np.sum(is_consonant_vec(matrix), axis=1)
    return matrix, np.mean(consonants / col)


def _analyze_cols(matrix):
    row, col = matrix.shape
    freq_matrix = np.zeros((col, col), dtype=int)

    for i, j in itertools.permutations(range(col), 2):
        col_i, col_j = matrix[:, np.array([i, j])].T
        bigram_cnt = np.sum(
            list(
                map(
                    lambda x: x in MOST_COMMON_CRO_BIGRAMS,
                    map(
                        lambda x: "".join(x), zip(col_i, col_j)
                    )
                )
            )
        )
        freq_matrix[i, j] = bigram_cnt
    return freq_matrix


def _calc_best_matrix(candidates):
    best_matrix, best_consonant_ratio, best_diff = None, 0, np.inf
    for row, col in candidates:
        matrix, consonant_ratio = _construct_matrix(row, col)
        diff = abs(consonant_ratio - .57)
        if best_diff > diff:
            best_matrix, best_consonant_ratio, best_diff = matrix, consonant_ratio, diff
    return best_matrix


def _filter(matrix):
    matrix[matrix < 2] = 0
    return matrix


def _cross_out(matrix, i, j):
    tmp = matrix[i][j]
    matrix[j, i] = 0
    matrix[i, :] = 0
    matrix[:, j] = 0
    matrix[i][j] = tmp
    return matrix


def _connect_tuples(order, first, ind):
    try:
        match = first.index(ind)
        result = _connect_tuples(order, first, order[match][1])
        return [order[match][0]] + result
    except ValueError:
        return [ind]


def _connect(order):
    first, second = zip(*order)
    starts = [i for i in first + second if (i in first and i not in second)]

    return [_connect_tuples(order, first, ind) for ind in starts]


def main():
    prime_facors = list(_calc_prime_factors(len(SIFRAT)))
    row_col_candidates = _calc_row_col(prime_facors, col_lb=4, col_ub=16)
    matrix = _calc_best_matrix(candidates=row_col_candidates)

    _print_matrix_with_ratios(matrix, header="Choosing:")

    freq_matrix = _analyze_cols(matrix)
    _print_matrix(freq_matrix, header="Frequency matrix")

    freq_matrix = _filter(freq_matrix)
    _print_matrix(freq_matrix, header="Frequency matrix w/o small frequencies")

    order = []
    for _ in range(freq_matrix.shape[1] - 1):
        i, j = map(int, input("Choose pair to add to permutation (separate with ','): ").split(","))
        assert freq_matrix[i][j] != 0
        freq_matrix = _cross_out(freq_matrix, i, j)

        order.append((i, j))

        result = _connect(order)
        _print_matrix(freq_matrix)

    assert len(result) == 1
    for i in np.ravel(matrix[:, np.array(result[0])]):
        print(i, end='')


if __name__ == '__main__':
    is_consonant_vec = np.vectorize(is_consonant)
    main()
