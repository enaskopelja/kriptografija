# Zadatak 1
> Odredite produkt polinoma 
`x^7 + x^6 + x^4 + x^2 + x + 1` i `x^6 + x^5 + x^2 + 1`
u polju `GF(28)`, definiranom kao `Z2[X]/(x^8 + x^4 + x^3 + x + 1).`

`(x^7 + x^6 + x^4 + x^2 + x + 1) * (x^6 + x^5 + x^2 + 1) = 1 + x^2 + x^3 + x^6 + x^8 + x^10 + x^12 + x^13`

konačno: `1 + x^2 + x^3 + x^6 + x^8 + x^10 + x^12 + x^13 (mod g(x)) = x^2 + x^3 + x^4 + x^6 + x^7`
`
# Zadatak 2
> Izračunajte:
>
> ```(C7 x^3 + E8 x^2 + C0 x + 43) ⊗ (9C x^3 + 4E x^2 + 8D x + 90).```

```
43 * 90 = x + x^3 + x^7
C7 * 8D = x + x^2 + x^3 + x^5 + x^6 + x^7
E8 * 4E = 1 + x + x^2 + x^3 + x^6
C0 * 9C = x^2 + x^4

C0 * 90 = 1 + x + x^5 + x^6
43 * 8D = x^2 + x^3 + x^5 + x^7
C7 * 4E = 1 + x + x^3 + x^4 + x^5 + x^6 + x^7
E8 * 9C = x + x^2 + x^3 + x^4 + x^7

E8 * 90 = x + x^4
C0 * 8D = x^5 + x^6
43 * 4E = x^2 + x^4 + x^6 + x^7
C7 * 9C = 1 + x^2 + x^3 + x^5 + x^6 + x^7

C7 * 90 = x + x^2 + x^3 + x^4 + x^5 + x^7
E8 * 8D = x^2 + x^4 + x^5 + x^6
C0 * 4E = x + x^3
43 * 9C = 1 + x + x^4 + x^5 + x^7
________________________________________
result:  ad
```
# Zadatak 3

>  Odaberite dva različita četveroznamenkasta prosta broja `p` i `q`. Neka
je `n = p · q`. Odaberite peteroznamenkasti broj `e` koji je relativno prost
sa `ϕ(n)`. 
> 
> Sifrirajte otvoreni tekst `x = 123407` pomoću RSA kriptosustava s javnim ključem `(n, e)`. Odredite pripadni
tajni ključ `d`.
```
(p, q) = (2719, 1373)
n = 2719 * 1373 = 3733187
phi(n) = 2718 * 1372 = 3729096
e = 95615
d = 95615^-1 (mod 3729096)= 1780559
y = e_K(123645) = 2772472
```