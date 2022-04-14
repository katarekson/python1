class Kaczka:
    
    def chodzenie(self):
        print("Kaczka chodzi")
        
    def odglos(self):
        print("Kaczka kwacze")
        
class Kurczak:
    
    def chodzenie(self):
        print("Kurczak chodzi")
        
    def odglos(self):
        print("Kurczak gdaka")
        
    
class Osoba():
    
    def zlapanie(self, kaczka):
        kaczka.chodzenie()
        kaczka.odglos()
        print("Zlapales ja!!")
        
kaczka = Kaczka()
kurczak = Kurczak()
osoba = Osoba()

osoba.zlapanie(kurczak)