class Telefon:
    
    def __init__(self,model,rok,kolor):
        self.model = model
        self.rok = rok
        self.kolor = kolor
    
    
    
    def przegladanie(self):
        print("Przegladasz "+self.model+"")
    
    def stop(self):
        print("Przestałeś przegladac "+self.model+"")