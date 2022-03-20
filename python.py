def dodaj(*liczby):
    sum = 0
    liczby = list(liczby)
    liczby[0] = 0
    for i in liczby:
        sum += i
    return sum
    
    


print(dodaj(1,2,3,10))