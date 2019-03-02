#`1234567890-=`
        #~!@#$%^&*()_+
        #{}[]
        #:"|";'\,./<>?

tekst = 'piotrWrtoip'

czy_palindrom = True

for indeks, literka in enumerate(tekst):
    
    if tekst [indeks] ==  tekst [-indeks-1]: 
        pass
            
    else:
        czy_palindrom  = False
        break

for indeks, literka in enumerate(tekst):
    
    if tekst [indeks] !=  tekst [-indeks-1]: 
        czy_palindrom  = False
        break

if czy_palindrom:
    print ('Tak, to jest palindrom')
else:
    print ('Nie, to nie jest palindrom')

for i in range(len(tekst)):
    
    if tekst [i] ==  tekst [-i-1]: 
        continue
            
    else:
        print ('nie jest palindromem')
        break

if tekst == tekst[::-1]:
    print(' jest palindromem') 






        
















