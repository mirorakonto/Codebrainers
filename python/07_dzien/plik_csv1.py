import csv

with open('przykladowy.csv', 'r') as f:
    czytacz = csv.reader(f) #czytacz i przeparsowanie pliku
    for wiersz in czytacz:
        print(wiersz)
        #od linii 7 zamkniety
        #global module index , domyslnie dzieli na przecinek, doczytac o funkcji reader

    






