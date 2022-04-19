sklep = [("Podkoszulka", 50.00),
         ("Spodnie", 129.00),
         ("Bluza", 259.00),
         ("Skarpetki", 23.00)]

to_pln = lambda data: (data[0],data[1]*4.64)
to_euro = lambda data: (data[0],data[1]/4.64)

sklep_euro = list(map(to_euro, sklep))

for i in sklep_euro:
    print(i)