uczestnik = 'Basia'

lista = ['Piotr', 'Aga', 'Basia']

for zmienna in lista:
    if zmienna == uczestnik:
        print('zmienna szukana jest', uczestnik)
    else:
        print ('nie znajduje się na liście', uczestnik)

        #`1234567890-=`
        #~!@#$%^&*()_+
        #{}[]
        #:"|";'\,./<>?

if uczestnik in lista:
    print ('zmienna szukana', uczestnik, 'nie znajduje się na liście')

for pozycja, uczen in enumerate(lista):
    print (pozycja, ': ', uczen)

print ('********', uczen)

for pozycja, uczen in enumerate(lista):
    if uczen == uczestnik:
        print (pozycja+1, ': ', uczen)

print ('********', uczen)  
