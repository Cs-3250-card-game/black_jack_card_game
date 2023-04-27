import tkinter as tk
import random

# Define constants
CARD_WIDTH = 73
CARD_HEIGHT = 97
CARD_SPACING = 10
DECK_SIZE = 52
PLAYER_X = 20
PLAYER_Y = 200
DEALER_X = 20
DEALER_Y = 20

# Create the main window
root = tk.Tk()
root.title("Blackjack")

# Create the canvas
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Create a deck of cards
deck = list(range(DECK_SIZE))
random.shuffle(deck)

# Create the player's hand
player_hand = []
player_score = 0

# Create the dealer's hand
dealer_hand = []
dealer_score = 0

# Create the card images
card_images = {}
suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
for suit in suits:
    for rank in ranks:
        filename = "cards/{}_{}.gif".format(rank, suit)
        card_images[(rank, suit)] = tk.PhotoImage(file=filename)

# Create the card labels
player_card_labels = []
dealer_card_labels = []
for i in range(2):
    player_card = deck.pop()
    player_hand.append(player_card)
    player_card_label = tk.Label(image=card_images[get_card(player_card)], bd=0)
    player_card_label.place(x=PLAYER_X+i*(CARD_WIDTH+CARD_SPACING), y=PLAYER_Y)
    player_card_labels.append(player_card_label)
    player_score += get_card_value(player_card)

    dealer_card = deck.pop()
    dealer_hand.append(dealer_card)
    dealer_card_label = tk.Label(image=card_images[get_card(dealer_card)], bd=0)
    dealer_card_label.place(x=DEALER_X+i*(CARD_WIDTH+CARD_SPACING), y=DEALER_Y)
    dealer_card_labels.append(dealer_card_label)
    dealer_score += get_card_value(dealer_card)

# Create the hit button
def hit():
    global player_score
    if player_score < 21:
        player_card = deck.pop()
        player_hand.append(player_card)
        player_card_label = tk.Label(image=card_images[get_card(player_card)], bd=0)
        player_card_label.place(x=PLAYER_X+len(player_hand)*(CARD_WIDTH+CARD_SPACING), y=PLAYER_Y)
        player_card_labels.append(player_card_label)
        player_score += get_card_value(player_card)
        if player_score > 21:
            result_label.config(text="You went over 21. You lose.")
            hit_button.config(state="disabled")
            stand_button.config(state="disabled")

# Create the stand button
def stand():
    global dealer_score
    while dealer_score < 17:
        dealer_card = deck.pop()
        dealer_hand.append(dealer_card)
        dealer_card_label = tk.Label(image=card_images[get_card(dealer_card)], bd=0)
        dealer_card_label.place(x=DEALER_X+len(dealer_hand)*(CARD_WIDTH+CARD_SPACING), y=DEALER_Y)
        dealer_card_labels.append(dealer_card_label)
        dealer_score += get_card_value(dealer_card)
    if dealer_score > 21:
        result_label.config(text="Dealer went over 21. You win!")
    elif dealer_score >= 17:
        result_label.config(text="Dealer got 21")
