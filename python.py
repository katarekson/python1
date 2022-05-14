from multiprocessing import Process, cpu_count 
import time


def licznik(num):
    count = 0
    while count < num:
        count += 1


def main():
    
    print(cpu_count())
    
    a = Process(target=licznik, args=(25000000000,))
    a.start()
    
    b = Process(target=licznik, args=(25000000000,))
    b.start()
    
    c = Process(target=licznik, args=(25000000000,))
    c.start()
    
    d = Process(target=licznik, args=(25000000000,))
    d.start()
    
    e = Process(target=licznik, args=(25000000000,))
    e.start()
    
    f = Process(target=licznik, args=(25000000000,))
    f.start()
    
    g = Process(target=licznik, args=(25000000000,))
    g.start()
    
    h = Process(target=licznik, args=(25000000000,))
    h.start()
    
    a.join
    b.join
    c.join
    d.join
    e.join
    f.join
    g.join
    h.join
    
    print("Zakończono w: ", time.perf_counter(), " sekund")


if  __name__ == '__main__':
    main()