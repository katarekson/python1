<<<<<<< HEAD
class Zwierze:
    
    def jedzenie(self):
        print("To zwierze je")
        
class Zajac(Zwierze):
    def jedzenie(self):
        print("Ten zajac je marchewke")

zajac = Zajac()
zajac.jedzenie()
=======
class Ofiara:
    
    def ucieknij(self):
        print("To zwierze ucieka")
        
class Lowca:
    
    def polowac(self):
        print("To zwierze poluje")


class Krolik(Ofiara):
    pass

class Orzel(Lowca):
    pass

class Ryba(Lowca, Ofiara):
    pass

krolik = Krolik()
orzel = Orzel()
ryba = Ryba()

krolik.ucieknij
orzel.poluje
>>>>>>> 4d588c1022d5566eb3c8bf94725269f0497737c4
