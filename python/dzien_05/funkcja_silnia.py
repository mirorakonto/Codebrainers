def silnia(n):
    wynik = 1
    for a in range(2,n+1):
        wynik *= a

    return wynik

liczba=silnia(5)
print(liczba)

