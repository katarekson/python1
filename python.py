class Zwierze:
    
    def jedzenie(self):
        print("To zwierze je")
        
class Zajac(Zwierze):
    def jedzenie(self):
        print("Ten zajac je marchewke")

zajac = Zajac()
zajac.jedzenie()