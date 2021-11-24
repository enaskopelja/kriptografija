from commons import reverse_lookup, lookup
from dictionary import most_common_next_letter


def _match(*, p1_candidates, l1, l2, p2_candidates=None):
    if p2_candidates is None:
        p2_candidates = p1_candidates

    for p1 in p1_candidates:
        p2 = lookup((reverse_lookup(l2) - reverse_lookup(l1) + reverse_lookup(p1)) % 26)
        if p2 in p2_candidates:
            yield p1, p2


def _merge(solution, candidate, ask=False):
    for p1, p2 in solution:
        if not ask or input(f"{p1}, {p2}, {candidate}") == "k":
            yield p1 + candidate[0], p2 + candidate[1]


def _filter(solution):
    to_remove = set()

    for c in solution:
        if input(f"should remove {c}?") != "x":
            to_remove.add(c)
    return solution.difference(to_remove)


def _list_solution(*, index, solution):
    print(f"Kandidati duljine {index + 1}:")
    for s in solution:
        print(*s, end=", ")
    print()


def main(*, e1, e2, silent=False):
    solution = {('', '')}
    for index, candidates in enumerate(["SPND", "AEIOUR"]):
        solution = {
            x
            for match in _match(p1_candidates=candidates, l1=e1[index], l2=e2[index])
            for x in _merge(solution, match)
        }
        if not silent:
            _list_solution(index=index, solution=solution)

    for index in range(2, len(e1)):
        solution = {
            (p1 + x1, p2 + x2) for p1, p2 in solution for x1, x2 in _match(
                p1_candidates=most_common_next_letter(p1, len(e1), k=10),
                p2_candidates=most_common_next_letter(p2, len(e1), k=10),
                l1=e1[index],
                l2=e2[index],
            )
        }
        if not silent:
            _list_solution(index=index, solution=solution)
    return solution


def _test():
    result = main(e1="CRUDLHGCAS", e2="XVXDUXKUIA", silent=True)
    assert len(result) == 1
    assert 'NEPOBJEDIV', 'SAMOSTALAN' == sorted(result.pop())


if __name__ == '__main__':
    _test()
    main(e1="TYHKXPWB", e2="RHVAKWES")
