import csv

with open('przykladowy.csv', 'r') as f:
    czytacz = csv.DictReader(f) #czytacz i przeparsowanie pliku

    lista_years =[]
    Lista_scores = []

    for wiersz in czytacz:
        #print(wiersz) #wiersz = OrderedList
        #od linii 7 zamkniety

        #global module index , domyslnie dzieli na przecinek, doczytac o funkcji reader
        #print(wiersz)
    #DictReader potrafi rozpoznaczc wiersz naglowkowy, dostepnosc pod nazwami kolumn, DictReader nie tworzy slownika
    #a slownik nie trzyma kolejnosci
    #typ danych   OrderedDIct
        

        konw_int_rok = int(wiersz['Year'])
        lista_years.append(konw_int_rok)
        konw_int_wynik = int(wiersz['Score'])
        Lista_scores.append(konw_int_wynik)

        #years.append(int(year))
        #scores.append(int(score))

    print(lista_years)
    print(Lista_scores)

    minimalny_wynik = Lista_scores[0]
    minimalny_wynik_rok = lista_years[0]
    maksymalny_wynik = Lista_scores[0]
    maksymalny_wynik_rok = Lista_scores[0]


    for rok, wynik in zip(lista_years, Lista_scores):
        print('W roku ', rok, ' mial wynik ', wynik)
        #czy ten wynik jest mniejszy od najmniejszego dotychczasowego wyniku?
        if minimalny_wynik > wynik:
            minimalny_wynik = wynik
            minimalny_wynik_rok = rok

        if maksymalny_wynik < wynik:
            maksymalny_wynik = wynik
            maksymalny_wynik_rok = rok
             

            
    print("Rok z najnisza ocena" , minimalny_wynik, 'to: ', minimalny_wynik_rok)
     
    print("Rok z najwyzsza ocena" , maksymalny_wynik, 'to: ', maksymalny_wynik_rok)

    suma = 0
    for wynik in Lista_scores:
        suma = suma + wynik

    srednia = suma / len(Lista_scores)   

    print(srednia) 

    



















        # 1. przekonwertowac na inty
        # 2. Dodawac do listy
        # 3. Wypisz kazda liste do sprawdzenia
        # 4. Rok z minimalnym scorem
        # 5. ROk z maksymalnym scorem
        # 6. Srednia wartosc wyniku
        # 7. Mediana - dane uporzadkowac - funkcja sorted.
        # petla for, zip tez moze byc uzyty





#append rozszerzanie listy, element po elemenencie idziemy


