import os

zrodlo = "folder" 
cel = "C:\\Users\\Miros\\Desktop\\folder"

try:
    if os.path.exists(cel):
        print("Juz istnieje tam taki plik!")
    else:
        os.replace(zrodlo,cel)
        print(zrodlo +" zostalo tam przeniesione")
except FileNotFoundError:
    print(zrodlo +" nie zostalo znalezione")