#spytac usera o nazwe pliku
nazwa_pliku = input('Podaj nazwe pliku: ')
#spytac o tresc
tresc = input('Podaj tresc twojego pliku: ')

# tresc = tresc + '\n'
tresc += "\n"

#utworzyc plik i zapisac
with open(nazwa_pliku, 'w') as f:
    f.write(tresc)

