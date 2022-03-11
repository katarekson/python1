wiek = int(input("Ile masz lat?: "))

if wiek == 100:
    print("Ale jestes stary")
elif wiek >= 18:
    print("Jestes dorosly")
elif wiek < 0:
    print("Jescze sie nie urodziles")
else:
    print("Jestes bobaskiem")
