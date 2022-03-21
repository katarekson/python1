import os

path = "C:\\Users\\Miros\\folder"

if os.path.exists(path):
    print("To istnieje!")
    if os.path.isfile(path):
        print("To jest plik!")
    elif os.path.isdir(path):
        print("To jest folder!")
else:
    print("To nie istnieje!")