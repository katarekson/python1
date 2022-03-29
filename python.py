import random


while True:
    wybory = ["papier","kamien","nozyce"]

    komputer = random.choice(wybory)
    gracz = None

    while gracz not in wybory:
        gracz = input("papier, kamien czy nozyce?: ").lower()


    if gracz == komputer:
        print("Komputer: ", komputer)
        print("Gracz: ", gracz)
        print("Remis")
    elif gracz == "kamien":
        if komputer == "papier":
            print("Komputer: ", komputer)
            print("Gracz: ", gracz)
            print("przegrales")
        if komputer == "nozyce":
            print("Komputer: ", komputer)
            print("Gracz: ", gracz)
            print("Wygrales")
    elif gracz == "papier":
        if komputer == "nozyce":
            print("Komputer: ", komputer)
            print("Gracz: ", gracz)
            print("przegrales")
        if komputer == "kamien":
            print("Komputer: ", komputer)
            print("Gracz: ", gracz)
            print("Wygrales")
    elif gracz == "nozyce":
        if komputer == "kamien":
            print("Komputer: ", komputer)
            print("Gracz: ", gracz)
            print("przegrales")
        if komputer == "papier":
            print("Komputer: ", komputer)
            print("Gracz: ", gracz)
            print("Wygrales")
            
    zagraj_ponownie = input("Chcesz zagrac ponownie? (tak/nie) ").lower()
    
    if zagraj_ponownie != "tak":
        break
    
print("Zegnaj")