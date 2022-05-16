from tkinter import *

okno = Tk()
# okno.geometry("1000x500")
okno.title("Halal piesus")
zdjecie = PhotoImage(file='C:\\Users\\Miros\\Downloads\\piesus.png')

label = Label(okno, 
              text="Haram halal bismillah mashallah", 
              font=('Arial',60,'bold'),
              fg='blue',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=zdjecie,
              compound='bottom',)

label.pack()
# label.place(x=100,y=100)


okno.mainloop()