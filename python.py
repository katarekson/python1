# def podwoj(x):
#     return x * 2

# print(podwoj(10))

podwoj = lambda x: x * 2
pomnoz = lambda x, y: x * y
dodaj = lambda x, y, z: x + y + z
pelne_imie = lambda imie, nazwisko: imie+" "+nazwisko
sprawdzenie_wieku = lambda wiek: print("Mozesz sie zarejestrowac") if wiek >= 18 else print("Nie masz ukonczonych 18 lat")
print(sprawdzenie_wieku(19))