student = ("Miroslaw",16,"Mezczyzna")

print(student.count("Miroslaw"))
print(student.index("Mezczyzna"))

for x in student:
    print(x)
    
if "Miroslaw" in student:
    print("Miroslaw jest super")