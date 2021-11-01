from commons import count_n_grams

cypher = """
PFYFC EWBWA SBZNX XCUWI NCEPG DNCWC EMPZE UWGPS
DUWUW DCIFV UWVUW DTPVP CDTWP RMPBN UDOEW MWCPC
EPGRU PSDGN UVDZC DXPAP COPEA PNUWT PCWCP ONBAD
IENPV PRDMN OONMW TNSDT NDCIA PGVNY CFTPN VWBNO
BADIE NCFCE PGF
""".replace(' ', '').replace('\n', '')

test = {
    "P": "A",
    "Q": "B",
    "S": "C",
    "T": "D",
    "W": "E",
    "X": "F",
    "Y": "G",
    "Z": "H",
    "D": "I",
    "U": "J",
    "B": "K",
    "R": "L",
    "O": "M",
    "V": "N",
    "N": "O",
    "I": "P",
    "K": "Q",
    "A": "R",
    "C": "S",
    "E": "T",
    "F": "U",
    "G": "V",
    "H": "W",
    "J": "X",
    "L": "Y",
    "M": "Z",
}


def match_enc_dec(n: int, k: int = 10):
    for x in count_n_grams(cypher, n).most_common(k):
        if x[1] == 1 and n > 1:
            break

        print(*x, ''.join(test.get(xx, ' ') for xx in x[0]))
    print()


# A, I, O, E, N
# JE, NA, RA, ST, AN, NI, KO, OS, TI, IJ, NO, EN, PR
# IJE, STA, OST, JED, KOJ, OJE, JEN
#

if __name__ == '__main__':
    map(match_enc_dec, range(4))
    print(cypher)
    for i in cypher:
        print(test.get(i, " "), end="")
    print()
