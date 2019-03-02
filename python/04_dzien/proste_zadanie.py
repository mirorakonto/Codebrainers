 #`1234567890-=`
        #~!@#$%^&*()_+
        #{}[]
        #:"|";'\,./<>?

for zmienna in range(1, 101):
    print(zmienna)


for zmienna in range(1, 101):
    if zmienna% 3 ==0 and zmienna% 5 == 0:
        print (zmienna, ': FizzBuzz') 
    elif zmienna% 5 == 0:
        print (zmienna, ': Buzz')
    elif zmienna% 3 == 0:
        print (zmienna, ': Fizz')
    else:
        print(zmienna) 
        








