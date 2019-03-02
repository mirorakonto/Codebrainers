tekst = "Ala ma kota a kot ma AlęX"

#`1234567890-=`
        #~!@#$%^&*()_+
        #{}[]
        #:"|";'\,./<>?


wystapienia = dict()
# wystapienia(literka) +=1

for i in tekst:
    if i in wystapienia:
        wystapienia[i] +=1
    else:
        wystapienia[i] = 1


print(wystapienia)   
 







