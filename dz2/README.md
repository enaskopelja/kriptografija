# Zadatak 1
________________

> Vigenereovom sifrom iz otvorenog teksta na hrvatskom jeziku dobiven
je sifrat:

```UEOIB HFUAE BUVKZ JRLPK NAQAC HTLCR QEWIV MNHBR
YEUIV RPRCV NSHZR MIPAK HZDKI HPWOC NGLJL QJHSR
UAMUT HMDLV NGOAJ DUQOM HNDMR MENIF CTLHF FLDSR
AIOIJ TSLFI HRDNZ OAMES ZZHRZ DSQJZ GOYID CENRZ
OTLRR MJHMQ ZBDVC IARPI HJDTV KJH
```

>Odredite najprije duljinu kljucne rijeci, potom samu kljucnu rijec, te
dekriptirajte sifrat.

## Rjesenje:
Prosjecni indeksi koincidencije:
```
m: 2	->	0.043
m: 3	->	0.044
m: 4	->	0.044
m: 5	->	0.065
m: 6	->	0.044
m: 7	->	0.039
m: 8	->	0.051
m: 9	->	0.046
m: 10	->	0.065
m: 11	->	0.042
m: 12	->	0.044
m: 13	->	0.044
m: 14	->	0.036
m: 15	->	0.071
m: 16	->	0.043
m: 17	->	0.034
m: 18	->	0.045
m: 19	->	0.041
```

Vidimo da se IC znacajno povecava na visekratnicima broja 5, slutimo `m = 5`.

Analizom medusobnog indeksa koincidencije dobivamo sljedecu matricu, u i-tom stupcu nalaze se (u silaznom poretku od najvjerojatnijeg u nultom retku do manje vjerojatnog u drugom)
najvjerojatnija i-ta slova kljuca.
```
0 1 2 3 4
Z A D A R
U F Z I I
D R H R V
```
Ocito je:
`Kljuc = ZADAR`

Otvoreni tekst:
```
VELIKI FRANCUSKI KRIPTOANALITICAR ETIENNE 
BAZERIES POCEO SE ZANIMATI ZA KRIPTOLOGIJU
RJESAVAJUCI MALE OGLASE U NOVINAMA NEKI OD
TIH OGLASA BILI SU SIFRIRANI PA JE BAZERIES 
NJIHOVIM DEKRIPTIRANJEM ZABAVLJAO PRIJATELJE
```

# Zadatak 2
______________________________
> Sifrirajte otvoreni tekst `FRIEDMAN` pomocu Playfairove sifre s kljucnom rijeci `CRYPTOGRAPHY`

## Rjesenje

Matrica:
```
C R Y P T
T O G A H
D E F I J
K L M N Q
S U V X Z
```

### Sifriranje:
`FR` -(X)-> `EY` 

`IE` -(isti redak)-> `JF`

`DM` -(X)-> `FK`

`AN` -(isti stupac)-> `IX`


**Sifrat**: `EYJFFKIX`

# Zadatak 3
__________________
>Odredite kljuc K u Hillovoj sifri ako je poznato da je `m = 2`, te da
otvorenom tekstu `VERNAM` odgovara sifrat `DUCTKY`.

## Rjesenje
```
X = 
| 21  4 |
| 17 13 |
```

```
e(X) = 
| 3  20 |
| 2  19 |
```

```
X^-1 = 
| 13  10 |
| 23  19 |
```

#### Konacno:
```
K = 
| 7   8 |
| 3  15 |
```

# Pokretanje koda
`pip install -r requirements.txt`

`python3 PYTHONPATH=$PWD python3 dz2/z${BROJ_ZADATKA}.py`