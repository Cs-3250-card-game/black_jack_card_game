#Author: James L.
#Page 1 for Blackjack game GUI

from tkinter import *
from tkinter import ttk
import tkinter as tk

#main window
main = tk.Tk()

#title for main
main.title("21 Can You Do Something For Me")

#setup rows and columns
for i in range(3):
    main.columnconfigure(i, weight = 1, minsize = 35)
    main.rowconfigure(i, weight= 1, minsize = 35)

#welcome message label
welcLabel = tk.Label(master = main, text = "Welcome!\nEnter your name below:", relief = GROOVE)
welcLabel.grid(row = 0, column = 1, pady = 3)

#frame for name-entering area
nameArea = tk.Frame(master = main)
nameArea.grid(row = 1, column = 1)

#name entry box
nameBox = tk.Entry(master = nameArea, width = 20)
nameBox.pack(side = tk.LEFT)

#sets users name
nameSet = tk.Button(master = nameArea, text = "Set Name")
nameSet.pack(side = tk.LEFT)

#confirms users name
nameConfirm = tk.Label(master = main, text = "This label confirms the users name choice", 
                       relief = SUNKEN)
nameConfirm.grid(row = 2, column = 1)

#informs user of what to do next
moneyLabel = tk.Label(master = main, text = "Please select the amount you would\nlike to start with:",
                      relief = GROOVE)
moneyLabel.grid(row = 3, column = 1)

#frame for monetary options
moneyOption = tk.Frame(master = main)
moneyOption.grid(row = 4, column = 1)

#fifty dollar option button
fiftyOption = tk.Button(master = moneyOption, text = "$50", 
                        height=4, width=15)
fiftyOption.pack(side = tk.LEFT, fill = tk.BOTH, expand = TRUE)

#one hundred dollar option
hundredOption = tk.Button(master = moneyOption, text = "$100", 
                          height=4, width=15)
hundredOption.pack(side = tk.LEFT, fill = tk.BOTH, expand = TRUE)

#two hundred dollar option
twoHunOption = tk.Button(master = moneyOption, text = "$200", 
                         height=4, width=15)
twoHunOption.pack(side = tk.LEFT, fill = tk.BOTH, expand = TRUE)

#confirms monetary choice
moneyConfirm = tk.Label(master = main, text = "This label confirms the users money choice",
                        relief = SUNKEN)
moneyConfirm.grid(row = 5, column = 1, pady = 4)

#starts game
start = tk.Button(master = main, text = "Start Game", height = 4, width = 10)
start.grid(row = 6, column = 1)

main.mainloop()

