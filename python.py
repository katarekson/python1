class Prostokat:
    def __init__(self,dlugosc,szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        

class Kwadrat(Prostokat):   
    
    def __init__(self,dlugosc,szerokosc):
        super().__init__(dlugosc,szerokosc)
    
    def pole(self):
        return self.dlugosc*self.szerokosc
class Kostka(Prostokat):
    def __init__(self,dlugosc,szerokosc,wysokosc):
        super().__init__(dlugosc,szerokosc)
        self.wysokosc = wysokosc
    
    
    def objetosc(self):
        return self.dlugosc*self.szerokosc*self.wysokosc


kwadrat = Kwadrat(4, 2)
kostka = Kostka(3, 1, 5)


print(kwadrat.pole())
print(kostka.objetosc())