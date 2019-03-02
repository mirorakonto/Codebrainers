lista = [3,4,5,6,7]

suma = 0
liczba_zmiennych = len(lista)

for zmienna in lista:
    suma = suma+zmienna

#print(suma) 

#srednia arytmetyczna
srednia = suma/liczba_zmiennych
print('srednia arytmetyczna liczb wynosi: ', srednia)

#suma = suma + 1

#srednia harmoniczna

#suma do harmonicznej
suma1 = 0
liczba_zmiennych1 = len(lista)
for zmienna in lista:
    suma1 = suma1 + (1/zmienna)
#print(suma1)

srednia1 = liczba_zmiennych1/suma1
print('srednia harmoniczna liczb wynosi: ', srednia1)

#srednia geometryczna
iloczyn = 1
liczba_zmiennych2 = len(lista)

for zmienna in lista:
    iloczyn = iloczyn * (zmienna)

srednia2 =  iloczyn  **(1/liczba_zmiennych2)
print('srednia geometryczna liczb wynosi: ', srednia2)



















    

