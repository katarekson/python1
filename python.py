# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def nowa_gra():
    
    odpowiedzi = []
    dobre_odpowiedzi = 0
    ilosc_pytan = 1
    
    for key in pytania:
        print("# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(key)
        for i in opcje[ilosc_pytan-1]:
            print(i)
        
        odpowiedz = input("Wybierz A, B lub C: ").upper()
        odpowiedzi.append(odpowiedz)
        
        dobre_odpowiedzi += sprawdz_odpowiedz(pytania.get(key),odpowiedz)
        ilosc_pytan += 1   
        
    pokaz_wynik(dobre_odpowiedzi, odpowiedzi)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def sprawdz_odpowiedz(rozwiazanie, odpowiedz):
    
    if rozwiazanie == odpowiedz:
        print("Dobrze")
        return 1
    else:
        print("Zle")
        return 0
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def pokaz_wynik(dobre_odpowiedzi, odpowiedz):
    print("# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Wyniki")
    print("# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    
    print("Ddpowiedzi: ", end="")
    for i in pytania:
        print(pytania.get(i), end=" ")
    print()
    
    print("Twoja odpowiedz: ", end="")
    for i in odpowiedz:
        print(i, end=" ")
    print()
    
    wynik = int((dobre_odpowiedzi/len(pytania))*100)
    
    print("Twoj wynik to: "+str(wynik)+"%")
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def zagraj_ponownie():
    
    pytanko = input("Chcesz zagrac ponownie? (tak/nie): ").lower()
    if pytanko == "tak":
        return True
    else:
        return False
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

pytania = {
    "Ile mam lat?": "C",
    "W ktorym roku zostal stworzony python?: ": "C",
    "Moja najulubiensza potrawa?: ": "A",
    "Imie mojego jeza?: ": "B"  
}


opcje = [["A. 15", "B. 18", "C. 50"],
         ["A. 2137", "B. 2000", "C. 1989"],
         ["A. Pizza", "B. Scampi", "C. Watrobka"],
         ["A. Jezyk", "B. Queen", "C. Pogczamp"]]

nowa_gra()

while zagraj_ponownie():
    nowa_gra()

print("Zegnaj")

