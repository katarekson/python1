from tkinter import *

def submit():
    nazwa = entry.get()
    print("Czesc "+nazwa)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get())-1 ,END)

okno = Tk()

entry = Entry(okno,
              font=("Comic Sans", 20),
              fg="blue",
              bg="black",
              show="*")

# entry.insert(0,'PODAJ IMIE')
entry.pack(side=LEFT)

submit_button = Button(okno, text="Zgodz sie",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(okno, text="Usun",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(okno, text="Cofnij",command=backspace)
backspace_button.pack(side=RIGHT)





okno.mainloop()