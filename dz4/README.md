# Zadatak 1
> Odredite produkt polinoma 
`x^7 + x^6 + x^5 + x^3 + x + 1` i `x6 + x4 + x + 1`
u polju `GF(28)`, definiranom kao `Z2[X]/(x^8 + x^4 + x^3 + x + 1).`

`(x^7 + x^6 + x^5 + x^3 + x + 1) * (x6 + x4 + x + 1) = 1 + x^2 + x^3 + x^6 + x^8 + x^10 + x^12 + x^13`

konačno: `1 + x^2 + x^3 + x^6 + x^8 + x^10 + x^12 + x^13 (mod g(x)) = x^2 + x^3 + x^4 + x^6 + x^7`

# Zadatak 2
> Izračunajte:
>
> ```(F4 x3 + D3 x2 + 31 x + F8) ⊗ (01 x3 + D2 x2 + 61 x + 03)```

```
F8 * 03 = 1 + x + x^4
F4 * 61 = x^2 + x^4
D3 * D2 = x^2 + x^3 + x^4 + x^5 + x^6 + x^7
31 * 01 = 1 + x^4 + x^5

31 * 03 = 1 + x + x^4 + x^6
F8 * 61 = x + x^2 + x^3 + x^5 + x^7
F4 * D2 = 1 + x^4 + x^5 + x^6 + x^7
D3 * 01 = 1 + x + x^4 + x^6 + x^7

D3 * 03 = x + x^2 + x^3 + x^5 + x^6
31 * 61 = 1 + x + x^2 + x^3 + x^4 + x^5 + x^7
F8 * D2 = x + x^2 + x^3 + x^4 + x^6
F4 * 01 = x^2 + x^4 + x^5 + x^6 + x^7

F4 * 03 = 1 + x + x^2
D3 * 61 = x^2 + x^3 + x^4 + x^5 + x^7
31 * D2 = x^3 + x^4 + x^6
F8 * 01 = x^3 + x^4 + x^5 + x^6 + x^7
________________________________________
result:  75
```
# Zadatak 3

>  Odaberite dva različita četveroznamenkasta prosta broja `p` i `q`. Neka
je `n = p · q`. Odaberite peteroznamenkasti broj `e` koji je relativno prost
sa `ϕ(n)`. 
> 
> Sifrirajte otvoreni tekst `x = 123645` pomoću RSA kriptosustava s javnim ključem `(n, e)`. Odredite pripadni
tajni ključ `d`.
```
(p, q) = (2719, 1373)
n = 2719 * 1373 = 3733187
phi(n) = 2718 * 1372 = 3729096
e = 95615
d = 95615^-1 (mod 3729096)= 1780559
y = e_K(123645) = 2772472
```