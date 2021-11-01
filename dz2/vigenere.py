from collections import Counter
from commons import lookup, cro_freqs, DIVIDER, reverse_lookup

cypher = """
UEOIB HFUAE BUVKZ JRLPK NAQAC HTLCR QEWIV MNHBR
YEUIV RPRCV NSHZR MIPAK HZDKI HPWOC NGLJL QJHSR
UAMUT HMDLV NGOAJ DUQOM HNDMR MENIF CTLHF FLDSR
AIOIJ TSLFI HRDNZ OAMES ZZHRZ DSQJZ GOYID CENRZ
OTLRR MJHMQ ZBDVC IARPI HJDTV KJH
""".replace(' ', '').replace('\n', '')


def _frequencies(text: str, absolute=True):
    counter = Counter(text)

    freqs = dict(counter)
    if not absolute:
        length = len(text)
        freqs = {k: v / length for k, v in freqs.items()}

    return freqs


def _coincidence_ind(text: str):
    """
        Ic(x) = ∑ fi(fi-1) / n(n-1).
    """
    n = len(text)

    return sum(
        i * (i - 1) for i in _frequencies(text).values()
    ) / (n * (n - 1))


def _avg_coincidence_ind(texts):
    return sum(
        map(_coincidence_ind, texts)
    ) / len(texts)


def _every_m(text: str, m: int):
    return [
        text[i::m]
        for i in range(m)
    ]


def _candidates_m(top_k: int = 3):
    return sorted(
        [
            (m, _avg_coincidence_ind(_every_m(cypher, m)))
            for m in range(2, 20)
        ],
        key=lambda x: x[1],
        reverse=True
    )[:top_k]


def _get_m():
    m_candidates = _candidates_m(top_k=3)
    print("Izbor m:")
    for c, ic in m_candidates:
        print(f"m={c:2d}\t->\tIC = {ic:.3f}")
    print(DIVIDER)

    return min(m_candidates, key=lambda x: x[0])[0]


def _get_key_letter(text, top_k: int = 1):
    """
    0 ≤ g ≤ 25 izračunamo

    Mg = ∑ pi f'i-g / n'.

    Mh = max { Mg : 0 ≤ g ≤ 25 }
    """
    freqs = _frequencies(text, absolute=False)

    return sorted(
        [
            (
                g, sum(
                    cro_freqs[lookup(i)] * freqs.get(lookup(i - g), 0)
                    for i in range(26)
                )
            )

            for g in range(26)
        ],
        key=lambda x: x[1],
        reverse=True
    )[:top_k]


def _get_key(m):
    m_caesars = _every_m(cypher, m)

    key_candidates = [
        list(
            map(lambda x: lookup((-x) % 26),
                (j[0] for j in _get_key_letter(m_caesars[i], top_k=3)))
        ) for i in range(m)
    ]
    print(" ".join(map(str, range(m))))
    for c in zip(*key_candidates):
        print(*c)
    print(DIVIDER)

    return "".join([c[0] for c in key_candidates])


def _decrypt(key: str):
    m = len(key)
    for i, c in enumerate(cypher):
        ord_c = reverse_lookup(c)
        ord_key = reverse_lookup(key[i % m])
        yield lookup(ord_c-ord_key)


def main():
    m = _get_m()
    key = _get_key(m)

    print("Kljuc: ", key)
    print("Otvoreni tekst: ", "".join(list(_decrypt(key))))


if __name__ == '__main__':
    main()
