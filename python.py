from tkinter import *

def submit():
    #print("Zamowiles: "+(listbox.get(listbox.curselection())))
    jedzenie = []
    
    for index in listbox.curselection():
        jedzenie.insert(index,listbox.get(index))
        
    for index in jedzenie:
        print("Zamowiles: "+index)
        
    
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())
    
def delete():
    #listbox.delete(listbox.curselection())
    
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
        
    listbox.config(height=listbox.size())
    
    
okno = Tk()

listbox = Listbox(okno, 
                  bg ="Black",
                  fg = "White",
                  font =('Constantia', 20),
                  width = 20,
                  selectmode=MULTIPLE, #pozwala na wybranie kilku
                  )




listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"burgir")
listbox.insert(1,"losos")
listbox.insert(1,"pomidorowa")
listbox.insert(1,"szpagetii")

listbox.config(height=listbox.size())

entryBox = Entry(okno)
entryBox.pack()

submit_button = Button(okno,text="submit",command=submit)
submit_button.pack()

add_button = Button(okno,text="dodaj",command=add)
add_button.pack()

del_button = Button(okno,text="usun",command=delete)
del_button.pack()

okno.mainloop()