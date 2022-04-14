from abc import ABC, abstractmethod


class Pojazd(ABC):
    
    @abstractmethod
    def jedz(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
class Auto(Pojazd):
    
    def jedz(self):
        print("Jedziesz autem")
        
    def stop(self):
        print("Auto sie zatrzymalo")
class Motor(Pojazd):
    
    def jedz(self):
        print("Jedziesz motocyklem")
        
    def stop(self):
        print("Ten motocykl sie zatrzymal")


# pojazd = Pojazd()
auto = Auto()
motor = Motor()


auto.stop()
motor.stop()