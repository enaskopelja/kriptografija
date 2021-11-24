# Zadatak 1
________________
> Dekriptirajte šifrat
> ```
> ITTUJ PSTAL NATCN RIUSK ENJIK EIMAD
> KOATU RAANI ITIAO VPSAL MAEJI CMARA
> PRSVO COOLS JKECR
> ```
> ako je poznato da je dobiven stupcanom transpozicijom iz otvorenog
teksta na hrvatskom jeziku, te da je broj stupaca veci od 4, a manji
od 16.

## Rjesenje
Duljina sifrata je `75 = 3 * 5 * 5`

Kandidati za dimenzije matrice koji zadovoljavaju uvjet na broj stupaca:
- `(5, 15)`
```
I P N R E E K R I V M C P C J  0.27:0.73
T S A I N I O A T P A M R O K  0.47:0.53
T T T U J M A A I S E A S O E  0.53:0.47
U A C S I A T N A A J R V L C  0.40:0.60
J L N K K D U I O L I A O S R  0.40:0.60
```
- `(15, 5)`
```
I R K V P  0.20:0.80
T I O P R  0.40:0.60
T U A S S  0.40:0.60
U S T A V  0.40:0.60
J K U L O  0.40:0.60
P E R M C  0.20:0.80
S N A A O  0.60:0.40
T J A E O  0.60:0.40
A I N J L  0.40:0.60
L K I I S  0.40:0.60
N E I C J  0.40:0.60
A I T M K  0.40:0.60
T M I A E  0.60:0.40
C A A R C  0.40:0.60
N D O A R  0.40:0.60
```

Srednji odnos samoglasnika i suglasnika je identican u obje matrice, `58.6%` suglasnika tj. `41.4%` samoglasnika, ipak dimenzija `(15, 5)` je nesto laksa za
analizu, a njezini omjeri su nesto konstantniji pa prvo pokusavamo s njom.

Matrica frekvencija:
```
- 2 9 3 1
2 - 4 4 2
6 5 - 3 3
5 3 4 - 3
4 5 0 2 -
```

Ako izbacimo frekvencije manje od 2:
```
- 2 9 3 -
2 - 4 4 2
6 5 - 3 3
5 3 4 - 3
4 5 - 2 -
```

Vidimo da je na poziciji `(0, 2)` najveca frekvencija dakle vjerojatno nakon `0` slijedi `2`. 
Uzevsi to u obzir dobivamo novu matricu (bez pozicija koje bi se kosile s odabirom slijeda `0,2`)
```
- - 9 - -
2 - - 4 2
- 5 - 3 3
5 3 - - 3
4 5 - 2 -
```

Sada se kao logican sljedeci izbor namece `(3, 0)` ili `(1, 3)` (najveci u retku i stupcu), nakon odabira obje opcije:
```
- - 9 - -
- - - 4 -
- 5 - - 3
5 - - - -
- 5 - - -
```

Konacno:
```
- - 9 - -
- - - 4 -
- - - - 3
5 - - - -
- 5 - - -
```
daje permutaciju: `41302` i otvoreni tekst:
> PRVI KRIPTOSUSTAV S AUTOKLJUCEM PRONASAO JE TALIJANSKI
> LIJECNIK I MATEMATICAR CARDANO

# Zadatak 2
______________________________

## Rjesenje

### Prvo slovo:
Iz informacije da obje poruke pocinju jednim od slova S, P, N, D. 

U slucaju zadana dva sifrata moguce kombinacije su:
```
S,Q
P,N
N,L
D,B
```
Vidimo da jedino `P, N` odgovara uvjetu. Dakle prva rijec pocinje s `P`, a druga s `N`

### Drugo slovo:

Promatramo najcesca druga slova u hrvatskom jeziku: `A`,`E`,`O`, `R`, `I` i `U`. 
Uvjete zadovoljavaju prefiksi:
1. `PI`, `NR`
2. `PR`, `NA`

Iako je `NR` validna opcija (gledano sa strane dekripcije zadane sifre), dalje nastavljamo s drugom kombinacijom 2 zbog
niske incidencije birama `NR` u hrvatskom jeziku.

Nadalje nastavljamo s trazenjem najvjerojatnijih nastavaka prefiksa kandidata, nuzno je uzeti barem 7 najvjerojatnijih jer
inace u koraku biranja kandidata za 4. slovo otpada `PRED`. 

U trazenju najvjerojatnijeg sljedeceg slova (uz neki zadani prefiks) sluzim se rjecnikom s http://rjecnik.hr/, kod u `dictionary.py`.

### Trece slovo:
moguci prefiksi: `PRS NAG, PRE NAS`

### Cetvrto slovo:
moguci prefiksi: 
```
PRSK NAGA 
PREV NASL 
PRES NASI 
PRED NAST 
PRET NASJ 
PREK NASA
``` 

### Peto slovo:
moguci prefiksi: `PRETR NASJE, PREDN NASTA` 

Za prvu rijec je u svakoj opciji samo po jedan kandidat: 
`PREDNOST` ili `PRETRAGA`.

Za drugu rijec kandidati su:
```
uz PRETRAGA: NASJESTI
uz PREDNOST: NASTAMBA, NASTANAK, NASTAVAK, NASTAVNI
```
### Sesto slovo:
Ostaje samo jedan moguci prefiks: `PREDNO NASTAV`

kandidati: `PREDNOST`,  `NASTAVAK, NASTAVNI` 

Prva rijec je `PREDNOST`.

### Sedmo slovo:
Ostaje samo po jedan kandidat za svaku rijec: `PREDNOST NASTAVAK` 

## Konacno:
```
PREDNOST 
NASTAVAK
``` 


# Zadatak 3
__________________
> Odredite skupove `test1(E1, E∗1, C'1)` i `test2 (E2, E∗2, C'2)` ako je 
> ```
> E1 = 000110, E∗1 = 110010, C'1 = 0001,
> E2 = 000010, E∗2 = 110110, C'2 = 1000.

## Rjesenje
> Kod u `z3.py`
```
Test 1:  000101 001001 011000 011001 101100 101101 110001 111101
Test 2:  001111 011111 101011 111011
```

# Pokretanje koda
`pip install -r requirements.txt`

`PYTHONPATH=$PWD python3 dz3/z${BROJ_ZADATKA}.py`