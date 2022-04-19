przyjaciele = [("Patrycja", 17),
               ("Kacper", 18),
               ("Krzysztof", 21),
               ("Karol", 20),
               ("Michal", 16)]


wiek = lambda data:data[1] >= 18 

przyjaciele_do_picia = list(filter(wiek, przyjaciele))

for i in przyjaciele_do_picia:
    print(i)