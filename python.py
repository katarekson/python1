from tkinter import *

def submit():
    print("Temperatura wynosi: "+ str(scale.get())+ " celcjusza")

okno = Tk()

scale = Scale(okno,
              from_=-10,
              to=50,
              length=500,
              orient=HORIZONTAL,
              font = ('Comic Sans', 15),
              tickinterval=10, #Liczby na skali
              showvalue = 0, #ukrywa wartosc
              troughcolor = 'green', #kolor slidera
              fg= 'red',
              bg= 'black',
              )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])

scale.pack()

button = Button(okno,text='Wyslij', command=submit)
button.pack()
okno.mainloop()