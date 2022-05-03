# #dluzsza wersja 
# kwadraty = []
# for i in range(1,11):
#     kwadraty.append(i * i)
# print(kwadraty)


# #list comprehension - krotsza wersja
# kwadraty = [i * i for i in range(1,11)]
# print(kwadraty)


studenci = [100,60,48,90,97,70,0]

# zdani_studenci = [x >= 60 for x in studenci]
# zdani_studenci = [i for i in studenci if i >= 60]
zdani_studenci = [i if i >= 60 else "niezdani" for i in studenci ]

print(zdani_studenci)