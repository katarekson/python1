class Zwierze:
    
    zyje = True
    
    def jedzenie(self):
        print("To zwierze je")
        
    def spanie(self):
        print("To zwierze spi")
        
class Zajac(Zwierze):
    def bieganie(self):
        print("Ten zajac biega")
class Ryba(Zwierze):
    def plywanie(self):
        print("Ta ryba pływa")
class Sowa(Zwierze):
    def latanie(self):
        print("Ta sowa lata")


zajac = Zajac()
ryba = Ryba()
sowa = Sowa()

zajac.bieganie()
ryba.plywanie()
sowa.latanie()