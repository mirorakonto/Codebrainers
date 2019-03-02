 #`1234567890-=`
        #~!@#$%^&*()_+
        #{}[]
        #:"|";'\,./<>?

lista = [0,1]
m = 6

for liczba in range(2, m+1):
    lista.append(lista[liczba-1]+lista[liczba-2])

print(lista)
print(m, " element to: ", lista[m])


