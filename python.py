import time

# print(time.ctime(10000000000))

# print(time.time())

# print(time.ctime(time.time()))

# czasownik = time.localtime()
# obiekt_czasowy = time.gmtime()
# print(czasownik)
# lokalny_czas = time.strftime("%Y-%m-%d %B %H:%M %S", czasownik)
# print(lokalny_czas)


# czasowy = "17 April, 2006"
# czasowy_obiekt = time.strptime(czasowy, "%d %B, %Y")
# print(czasowy_obiekt)

czasowy_tuple = (2006, 4, 20, 0, 6, 9, 0, 0, 0)
czasowy_string = time.asctime(czasowy_tuple,)
print(czasowy_string)


czasowy_tuple = (2006, 4, 20, 0, 6, 9, 0, 0, 0)
czasowy_string = time.mktime(czasowy_tuple,)
print(czasowy_string)