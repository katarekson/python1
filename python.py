class Auto:
    
    def wlaczanie(self):
        print("Silnik sie odpala")
        return self
    
    def jezdzenie(self):
        print("Jezdzisz autem")
        return self
        
    def hamulec(self):
        print("Naciskasz hamulec")
        return self
        
    def wylacz(self):
        print("Wylaczasz auto")
        return self
        
auto = Auto()

auto.wlaczanie()\
    .jezdzenie()\
    .hamulec()\
    .wylacz()
