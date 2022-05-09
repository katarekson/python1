import threading
import time

def sniadanie():
    time.sleep(3)
    print("Jesz sniadanie")
    
def kawa():
    time.sleep(4)
    print("Pijesz kawe")
    

def uczenie():
    time.sleep(5)
    print("Uczysz sie")

x = threading.Thread(target=sniadanie, args=())
x.start()
y = threading.Thread(target=kawa, args=())
y.start()
z = threading.Thread(target=uczenie, args=())
z.start()

x.join()
y.join()
z.join()

# sniadanie()
# kawa()
# uczenie()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())