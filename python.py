# #Akceptuje funkcje jako argument czyli funkcje glosno lub cicho jako argument po prostu

# def glosno(text):
#     return text.upper()

# def cicho(text):
#     return text.lower()

# def czesc(func):
#     text = func("Witam")
#     print(text)
    
# czesc(cicho)

def dzielnik(x):
    def dzielna(y):
        return y / x
    return dzielna

podziel = dzielnik(3)
print(podziel(11))