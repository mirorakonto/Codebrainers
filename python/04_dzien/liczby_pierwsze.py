#Wypiszliczby pierwsze sito Erastotenesa

sito = [True] * 100 #100 wartosci boolean o wartosci true na poczatku
sito[0]= False #wartosc brzegowa ktora jest zerem
#sito[1]=False #wartosc brzegowa ktora jest jedynka

for i in range(2,51): #[2,3,4,5,... 50]
    n=2
    wielokrotnosc = n * i
    while wielokrotnosc < 100:
        sito[wielokrotnosc] = False
        n += 1
        wielokrotnosc = n * i 

for indeks, wartosc in enumerate(sito):
    if wartosc ==True: #if wartosc: to jest to samo
        print("Liczba pierwsza: ", indeks)






