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