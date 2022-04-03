class organizm:
    
    zyje = True
    
class zwierze(organizm):
    
    def jedzenie(self):
        print("To zwierze je")
        
class pies(zwierze):
    
    def szczekanie(self):
        print("Pies szczeka")
        
pies = pies()
        
print(pies.zyje)

pies.jedzenie()
pies.szczekanie()