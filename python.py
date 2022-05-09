import threading
import time

def stoper():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Jestes zalogowany: ",count, "sekund")

x = threading.Thread(target=stoper, daemon=True)
x.start()

# x.setDaemon(True)

print(x.isDaemon())
odpowiedz = input("Chcesz wyjsc?")