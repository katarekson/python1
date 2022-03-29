import os
import shutil

lokalizacja = "test.txt"

try:
    # os.remove(lokalizacja)
    # os.rmdir(lokalizacja)
    # shutil.rmtree(lokalizacja)
except FileNotFoundError:
    print("Plik nie zostal znaleziony")
except PermissionError:
    print("Nie masz permisji zeby to usunac")
except OSError:
    print("Nie mozesz tego usunac korzystajac z tej funkcji")
else:
    print(lokalizacja + " zostalo usuniete")