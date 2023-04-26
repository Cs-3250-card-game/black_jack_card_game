from tkinter import *
import random

root = Tk()
root.geometry("900x500")
root.configure(background="#083605")

#Frame for cards
dealer_frame = LabelFrame(text="Dealer", bd=0)
dealer_frame.grid(row=1, column=1209, padx=90, ipadx=30)

player_frame = LabelFrame(text="Player", bd=0)
player_frame.grid(row=50, column=1209, padx=90, ipadx=30)

#Card on Frame
dealer_label = Label(dealer_frame, text="")
dealer_label.pack(pady=20)

player_label = Label(player_frame, text="")
player_label.pack(pady=20)

#Frame for money
bet_amount_frame = LabelFrame(text="Money", bd=0)
bet_amount_frame.grid(row=8, column=2000, padx=60, ipadx=60)

balance_amount_frame = LabelFrame(text="",bd=0)
balance_amount_frame.grid(row=30, column=2000, padx=64, ipadx=73)

#Money
bet_amount_label = Label(bet_amount_frame, text="Bet Amount:")
bet_amount_label.pack(pady=20)
balance_amount_label = Label(balance_amount_frame, text="Balance:")
balance_amount_label.pack(pady=20)

#Frame for button
#button_frame = Frame(root, bg="black")
#button_frame.pack(pady=20)

#Buttons
stand_button = Button(text="Stand")
stand_button.grid(row=5, column=4)

hit_button = Button(text="Hit")
hit_button.grid(row=6,column=4)

withdraw_button = Button(text="Withdraw", bg="#6e1212")
withdraw_button.grid(row=70,column=1499)


root.mainloop()
