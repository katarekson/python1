stolice = {'Polska':'Warszawa',
           'Japonia':'Tokio',
           'Rosja':'Moskwa'}

stolice.update({'Niemcy':'Berlin'})
stolice.update({'Polska':'Krakow'})
stolice.pop('Rosja')
stolice.clear()

# print(stolice['Niemcy'])

# print(stolice.get('Niemcy'))

# print(stolice.keys())

# print(stolice.values())

# print(stolice)

# print(stolice.items())

for key,value in stolice.items():
    print(key,value)