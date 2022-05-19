from tkinter import *

def display():
    if(x.get()=="TAK"):
        print("Zgodziles sie")
    else:
        print("Nie zgodziles sie")

okno = Tk()

# x = IntVar()
x = StringVar()

zdjecie = PhotoImage(file='C:\\Users\\Miros\\Downloads\\piesus.png')

check_button = Checkbutton(okno, 
                           text="Zgadzam sie na cos",
                           variable=x,
                           onvalue="TAK",
                           offvalue="NIE",
                           command=display,
                           font=('Comic Sans', 24),
                           fg='Blue',
                           bg='Black',
                           activeforeground='Blue',
                           activebackground='Black',
                           padx=25,
                           pady=20,
                           image=zdjecie,
                           compound='right')

check_button.pack()
okno.mainloop()