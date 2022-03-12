
temperatura = int(input("Jaka jest temperatura na dworze: "))

if not(temperatura >= 0 and temperatura <= 30):
    print("Temperatura jest zla")
    print("zostan w domu")
elif not(temperatura < 0 or temperatura > 30):
    print("Temperatura jest dobra!")
    print("wyjdz z domu prosze")
    