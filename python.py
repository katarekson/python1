# nazwy_uzytkownika = ["Mirek", "Kacper", "Michal"]
# haslo = ("zaq1@WSX", "niezlehaslo2137", "kulhaslo2305")

# uzytkownicy = dict(zip(nazwy_uzytkownika, haslo))

# print(type(uzytkownicy))

# for key,value in uzytkownicy.items():
#     print(key+" : "+value)
    
    
nazwy_uzytkownika = ["Mirek", "Kacper", "Michal"]
haslo = ("zaq1@WSX", "niezlehaslo2137", "kulhaslo2305")
data_logowania = ["01/03/2020","06/02/2021","16/03/2021"]

uzytkownicy = zip(nazwy_uzytkownika,haslo,data_logowania)

for i in uzytkownicy:
    print(i)