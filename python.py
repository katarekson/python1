from tkinter import *


jedzenie = ["pizza","burgir","stek"]

def zamowienie():
    if(x.get()==0):
        print("zamowiles pizze")
    elif(x.get()==1):
        print("zamowiles burgera")
    elif(x.get()==2):
        print("zamowiles steka")
    else:
        print("co?")

okno = Tk()


# obrazek_pizzy = PhotoImage(file='filepath')
# obrazek_burgira = PhotoImage(file='filepath')
# obrazek_steka = PhotoImage(file='filepath')
# obrazki_jedzenia = [obrazek_pizzy,obrazek_burgira,obrazek_steka]

x = IntVar()

for index in range(len(jedzenie)):
    radiobutton = Radiobutton(okno,
                              text=jedzenie[index], #dodaje tekst do pryzciskow
                              variable=x, #grupuje pryciski
                              value=index, #daje kazdemu przyciskowi wartosc
                              padx = 25,
                              pady = 15,
                              font = ('Comic Sans', 30),
                              #image = obrazki_jedzenia[index] #dodaje obrazek
                              #compound = 'right' #dodaje obrazek i tekst
                              indicatoron=0, #daje inny przycisk
                              width = 50,
                              command = zamowienie, #dzieki temu mamy komende
                              )
    radiobutton.pack(anchor=W)

okno.mainloop()