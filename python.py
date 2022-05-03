import functools


# literki = ["C","Z","E","S","C"]

# slowo = functools.reduce(lambda x, y,:x + y ,literki)
# print(slowo)

silnia = [5,4,3,2,1]

wynik = functools.reduce(lambda x, y,:x * y ,silnia)
print(wynik)