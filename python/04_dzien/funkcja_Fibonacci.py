def fibonacci(m):
    lista = [0,1]
    m = 6

    for liczba in range(2, m+1):
        lista.append(lista[liczba-1]+lista[liczba-2])
    
    return lista[m]

    #`1234567890-=`
        #~!@#$%^&*()_+
        #{}[]
        #:"|";'\,./<>?
wartosc = fibonacci(7)

print(wartosc)
