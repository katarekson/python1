# # sort() method = uzywane przy listach(lists)
# # sort() funcitons = uzywane przy iteracjach(iterables)

# # studenci = ["Mirek","Michal","Kacper","Krystian"]
# studenci = ("Mirek","Michal","Kacper","Krystian")


# # studenci.sort(reverse=True)
# sorted_studenci = sorted(studenci, reverse=True)

# for i in sorted_studenci:
#     print(i)

#-------------------------------------------------------------#
#-------------------------------------------------------------#
# # studenci = [("Mirek", "5", 16),
# #             ("Kacper","5", 17),
# #             ("Michal","4",16),
# #             ("Krystian","6",16)]

# ocena = lambda oceny:oceny[1]
# imie = lambda imiona:imiona[0]

# studenci.sort(key=imie, reverse=True)


# for i in studenci:
#     print(i)

#==============================================================#

    
    
studenci = (("Mirek", "5", 16),
             ("Kacper","5", 17),
             ("Michal","4",16),
             ("Krystian","6",16))

wiek = lambda wiek:wiek[2]
sorted_studenci = sorted(studenci, key=wiek)

for i in sorted_studenci:
    print(i)