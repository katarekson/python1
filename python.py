from tkinter import *

okno = Tk()

count = 0


def click():
    global count
    count+=1
    print("Kliknales przycisk B)")
    print("Stales sie tyle razy ziomem: ",count)
    
zdjecie = PhotoImage(file='C:\\Users\\Miros\\Downloads\\kok.png')

przycisk = Button(okno,
                  text="kliknij by stac sie ziomem!",
                  command=click,
                  font =("Comic Sans", 20),
                  fg='Blue',
                  bg='Black',
                  activeforeground='Blue',
                  activebackground='Red',
                  state=ACTIVE,
                  image=zdjecie,
                  compound='bottom',)
przycisk.pack()

window = mainloop()