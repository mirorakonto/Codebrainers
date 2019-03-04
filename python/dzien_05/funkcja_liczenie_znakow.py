def zliczanie(tekst)

    wystapienia = dict()

    for literka in tekst:
        if literka in wystapienia:
            wystapienia[literka] +=1
        else:
            wystapienia[literka]=1
    return wystapienia

wystapienia = zliczenia("Ala ma kota)
print wystapienia
 #`1234567890-=`
        #~!@#$%^&*()_+
        #{}[]
        #:"|";'\,./<>?

# def naszafunkcja(m):
# wynik to zmienna uzywana tylko w funkcji i nie istnieje poza nia
# wynik = m+2
# return zwraca wartosc zmiennej wynik
# return wynik

# wartosc obliczona przez funkcje naszafuncka jest zwracana
# i zapisywana do zmiennej wartosc
# wartosc = naszafunckja(Piotr)
#print(wartosc)

#wartosc = naszafunkcja(Marek)
#print(wartosc)
