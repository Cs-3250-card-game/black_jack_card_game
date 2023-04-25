from tkinter import *
import random

root = Tk()
root.title("21")
root.geometry("500x500")

card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
card_deck = [(value, suit) for value in card_values.keys() for suit in card_suits]
random.shuffle(card_deck)


class PlayerBase:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.ace_count = 0
        self.status = "playing"

    def deal_card(self):
        card = card_deck.pop()
        self.hand.append(card)
        self.score += card_values[card[0]]
        if card[0] == "A":
            self.ace_count += 1
        while self.score > 21 and self.ace_count > 0:
            self.score -= 10
            self.ace_count -= 1
        self.update_hand_label()

    def hit(self):
        self.deal_card()
        if self.score > 21:
            self.status = "bust"
    
    def update_hand_label(self):
        pass  # overridden by subclass


class Dealer(PlayerBase):
    def __init__(self):
        super().__init__()

    def update_hand_label(self):
        dealer_hand_label.configure(text=", ".join(card[0] + " of " + card[1] for card in self.hand))


class Player(PlayerBase):
    def __init__(self):
        super().__init__()

    def update_hand_label(self):
        player_hand_label.configure(text=", ".join(card[0] + " of " + card[1] for card in self.hand))


dealer = Dealer()
player = Player()

dealer_label = Label(root, text="Dealer's Hand:")
dealer_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

dealer_hand_label = Label(root, text=", ".join(card[0] + " of " + card[1] for card in dealer.hand))
dealer_hand_label.grid(row=0, column=1, padx=10, pady=10, sticky=W)

player_label = Label(root, text="Player's Hand:")
player_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

player_hand_label = Label(root, text=", ".join(card[0] + " of " + card[1] for card in player.hand))
player_hand_label.grid(row=1, column=1, padx=10, pady=10, sticky=W)

hit_button = Button(root, text="Hit", command=player.hit)
hit_button.grid(row=2, column=0, padx=10, pady=10)

stand_button = Button(root, text="Stand")
stand_button.grid(row=2, column=1, padx=10, pady=10)

status_label = Label(root, text="Status: " + player.status)
status_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

def stand():
    dealer_hand_label.configure(text=", ".join(card[0] + " of " + card[1] for card in dealer.hand))

    while dealer.score < 17:
        dealer.hit()

    if player.status == "bust":
        status_label.configure(text="Status: Player bust. You lose!")
    elif dealer.status == "bust":
        status_label.configure(text="Status: Dealer bust. You win!")
    elif player.score > dealer.score:
        status_label.configure(text="Status: You win!")
    elif dealer.score > player.score:
        status_label.configure(text="Status: You lose!")
    else:
        status_label.configure(text="Status: It's a tie!")
        
    hit_button.configure(state=DISABLED)
    stand_button.configure(state=DISABLED)

stand_button.configure(command=stand)

def deal_cards():
    dealer.deal_card()
    player.deal_card()

    dealer_hand_label.configure(text=", ".join(card[0] + " of " + card[1] for card in dealer.hand))
    player_hand_label.configure(text=", ".join(card[0] + " of " + card[1] for card in player.hand))
    
    if player.status == "bust":
        status_label.configure(text="Status: You bust. You lose!")
        hit_button.configure(state=DISABLED)
        stand_button.configure(state=DISABLED)

deal_cards()

def new_game():
    global dealer, player, card_deck
    card_deck = [(value, suit) for value in card_values.keys() for suit in card_suits]
    random.shuffle(card_deck)
    dealer = Dealer()
    player = Player()
    dealer_hand_label.configure(text="")
    player_hand_label.configure(text="")
    status_label.configure(text="")
    hit_button.configure(state=NORMAL)
    stand_button.configure(state=NORMAL)
    deal_cards()

deal_button = Button(root, text="Deal", command=new_game)
deal_button.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
