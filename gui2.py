# Name: Tri Nguyen

from tkinter import *

root = Tk()
root.geometry('900x700')
root.title("GUI #2 !")
# root.configure(bg = '#083605')

# HIT Button 
hit = Button(root, text = ' HIT ! ')
hit.place(x = 25, y = 550)
hit.pack

# STAND Button
stand = Button(root, text = ' STAND ! ')
stand.place(x = 25, y = 600)
stand.pack

# WITHDRAW Button
withdraw = Button(root, text = ' WITHDRAW SUM MONEY ! ')
withdraw.place(x = 25, y = 650)
withdraw.pack

# BET AMOUNT Label
betAmount = Label(root, text = ' BET AMOUNT: ')
betAmount.place(x = 700, y = 300)
betAmount.pack

# BALANCE Label
balance = Label(root, text = ' BALANCE: ')
balance.place(x = 700, y = 370)
balance.pack

# PLAYER CARDS 
card2 = Label(root, text = ' PLAYER CARD 1 ')
card2.place(x = 250, y = 430)
card2.pack

card4 = Label(root, text = ' PLAYER CARD 2 ')
card4.place(x = 470, y = 430)
card4.pack 

# COMPUTER CARDS
card1 = Label(root, text = ' COMPUTER CARD 1 ')
card1.place(x = 250, y = 200)
card1.pack

card3 = Label(root, text = ' COMPUTER CARD 2 ')
card3.place(x = 470, y = 200)
card3.pack 

# DECK of CARDS 
deck = Label(root, text = ' DECK ')
deck.place(x = 25, y = 50)
deck.pack

# Note
note = Label(root, text = ' NOTE: Need a minimum bet of $5')
note.place(x = 650, y = 25)

root.mainloop()