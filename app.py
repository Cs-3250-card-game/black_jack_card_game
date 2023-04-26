import tkinter as tk
from PIL import Image, ImageTk
import random

# Initialize the window
window = tk.Tk()
window.title("Blackjack")

# Create a frame for the game
game_frame = tk.Frame(window)
game_frame.pack()

# Load the card images
card_images = {}
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
for suit in suits:
    for rank in ranks:
        card_image = Image.open(f"cards/{rank}_of_{suit}.png")
        card_image = card_image.resize((70, 100), Image.ANTIALIAS)
        card_images[(rank, suit)] = ImageTk.PhotoImage(card_image)

# Initialize the deck
deck = [(rank, suit) for rank in ranks for suit in suits]

# Initialize the player's and dealer's hands
player_hand = []
dealer_hand = []

# Deal two cards to the player and dealer
for i in range(2):
    player_card = random.choice(deck)
    player_hand.append(player_card)
    deck.remove(player_card)
    dealer_card = random.choice(deck)
    dealer_hand.append(dealer_card)
    deck.remove(dealer_card)

# Create labels for the cards
player_card1_label = tk.Label(game_frame, image=card_images[player_hand[0]])
player_card1_label.pack(side="left")
player_card2_label = tk.Label(game_frame, image=card_images[player_hand[1]])
player_card2_label.pack(side="left")
dealer_card1_label = tk.Label(game_frame, image=card_images[dealer_hand[0]])
dealer_card1_label.pack(side="left")
dealer_card2_label = tk.Label(game_frame, image=card_images[("Back", "Red")])
dealer_card2_label.pack(side="left")

# Create a function to get the value of a card
def get_card_value(card):
    if card == "Ace":
        return 11
    elif card in ["Jack", "Queen", "King"]:
        return 10
    else:
        return int(card)

# Create a function for the player to hit
def hit():
    global player_hand, deck
    # Deal another card to the player
    player_card = random.choice(deck)
    player_hand.append(player_card)
    deck.remove(player_card)
    # Update the player's card labels
    player_card_label = tk.Label(game_frame, image=card_images[player_card])
    player_card_label.pack(side="left")
    # Check if the player has gone over 21
    if sum([get_card_value(card[0]) for card in player_hand]) > 21:
        result_label.configure(text="You went over 21! Dealer wins.")
        hit_button.configure(state="disabled")
        stand_button.configure(state="disabled")

# Create a function for the player to stand
def stand():
    global dealer_hand, deck
    # Reveal the dealer's hidden card
    dealer_card2_label.configure(image=card_images[dealer_hand[1]])
    # Deal cards to the dealer until their hand is greater than or equal to 17
    while sum([get_card_value(card[0]) for card in dealer_hand]) < 17:
        dealer_card = random.choice(deck)
        dealer_hand.append(dealer_card)
        deck.remove(dealer_card)
    # Update the dealer's card labels
    for i, card;
