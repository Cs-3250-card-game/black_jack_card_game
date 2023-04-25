from tkinter import *
from tkinter import ttk

win= Tk()

win.geometry("750x450")

win.title("BlackJack")

amount = 00.00

def restart():
    return

labelframe= LabelFrame(win, text= "BlackJack", font= ('Century 20 bold'),labelanchor= "n",bd=5,bg= "khaki3",width= 600, height= 450, cursor= "target")
labelframe.pack(expand= True, fill= BOTH)

l1= Label(labelframe, text="You're Out of Money", font= ('Century 20'), bg="khaki3")
l1.place(relx= .32, rely= .1)

l2= Label(labelframe, text= "$" + str(amount), font= ('Century 20'), bg="white")
l2.place(relx= .45, rely= .25)

b1= Button(win, text= "Try Again?", font= ('Century 20 bold'), fg="white", bg="red", command= restart)
b1.place(relx=.20, rely= .62)

b2= Button(win, text= "Give Up", font= ('Century 20 bold'), fg="white", bg="black", command= win.destroy)
b2.place(relx=.60, rely= .62)

win.mainloop()