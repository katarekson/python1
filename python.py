class Auto:
    
    kolor = None
    
class Motocykl:
    
    kolor = None
    
    
def zmien_kolor(pojazd, kolor):
    
    pojazd.kolor = kolor
    
auto_1 = Auto()
auto_2 = Auto()
auto_3 = Auto()

rower_1 = Motocykl()

zmien_kolor(auto_1, "czerwony")
zmien_kolor(auto_2, "fioletowy")
zmien_kolor(auto_3, "czarny")
zmien_kolor(rower_1, "czarny")

print(auto_1.kolor)
print(auto_2.kolor)
print(auto_3.kolor)
print(rower_1.kolor)