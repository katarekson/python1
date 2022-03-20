import random

x = random.randint(1,100)
y = random.random()

mojalista = ['papier','kamien','nozycze']
z = random.choice(mojalista)

karty = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(karty)

print(karty)


print(z)
print(x)
print(y) 