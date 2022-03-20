try:
    numerator = int(input("Podaj liczbe do podzielenia: "))
    denominator = int(input("Podaj liczbe przez ktora bedziesz dzielil: "))
    wynik = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("Nie mozesz dzielic przez zero!")
except ValueError as e:
    print(e)
    print("Podawaj tylko liczby")
except Exception as e:
    print(e)
    print("Cos poszlo nie tak")
else:
    print(wynik)
finally:
    print("To zawsze sie wykona!")