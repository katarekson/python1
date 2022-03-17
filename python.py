from symtable import Symbol


rows = int(input("Jak duzo rzedow?: "))
columns = int(input("Jak duzo Kolumn?: "))
symbol = input("Podaj symbol jaki chcesz uzyc: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()