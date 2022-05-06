# -----------------------------------------------------------------------

# miasta_w_C = {'Krakow': 24, 'Warszawa': 20, 'Poznan':28, 'Lodz':25}

# miasta_w_F= {key: round((value*1.8)+32) for (key,value) in miasta_w_C.items()}

# print(miasta_w_F)

# -----------------------------------------------------------------------

# miasta_pogoda = {'Krakow': "Slonce", 'Warszawa': "Slonce", 'Poznan': "Pada", 'Lodz': "Burza"}

# Sloneczne_miasta = {key: value for (key,value) in miasta_pogoda.items() if value == "Slonce"}

# print(Sloneczne_miasta)

# -----------------------------------------------------------------------

# miasta = {'Krakow': 24, 'Warszawa': 20, 'Poznan':28, 'Lodz':25}

# opis_miasta = {key: ("Cieplo" if value >= 23 else "zimno") for (key,value) in miasta.items()}

# print(opis_miasta)

# -----------------------------------------------------------------------

def sprawdz_temp(value):
    if value >=25:
        return "Goraco"
    elif 24>= value >=15:
        return "Cieplo"
    else:
        return "Zimno"

miasta = {'Krakow': 24, 'Warszawa': 20, 'Poznan':28, 'Lodz':25, 'Zakopane': 14}

opis_miasta = {key: sprawdz_temp(value) for (key,value) in miasta.items()}

print(opis_miasta)