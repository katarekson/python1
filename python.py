nazwa = "Miroslaw Klaus"

# pierwsze_imie = nazwa[7] liczba = litera w nazwie

# imie = nazwa[:8] od poczatku do 8 [poczatek:3]
# nazwisko = nazwa[9:] od 9 do konca [9:koniec]
# dziwne_imie = nazwa[::1] pokazuje wszystko [poczatek:koniec:co ile]
# odwrocone_imie = nazwa[::-1] pokazuje na odwrot [poczatek:koniec:-1]


strona_internetowa1 = "http://google.com"
strona_internetowa2 = "http://wikipedia.com"

slice = slice(7,-4)

print(strona_internetowa1[slice])
print(strona_internetowa2[slice])