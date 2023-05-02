import tkinter as tk
from PIL import Image, ImageTk
import random

# Initialize the main window
window = tk.Tk()
window.title("Blackjack")

# Initialize the deck
deck = []

# Create a function to get the value of a card
def get_card_value(card):
    if card == "Ace":
        return 11
    elif card in ["Jack", "Queen", "King"]:
        return 10
    else:
        return int(card)

# Create a function to deal cards to a hand
def deal_card(hand):
    global deck
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

# Create a function to update the score
def update_score(hand, score_label):
    score = sum([get_card_value(card[0]) for card in hand])
    for card in hand:
        if card[0] == "Ace" and score > 21:
            score -= 10
    score_label.configure(text=f"Score: {score}")

# Create a function to check if a hand is a blackjack
def is_blackjack(hand):
    if len(hand) == 2 and sum([get_card_value(card[0]) for card in hand]) == 21:
        return True
    else:
        return False

# Create a function to check if a hand has busted
def has_busted(hand):
    if sum([get_card_value(card[0]) for card in hand]) > 21:
        return True
    else:
        return False

# Create a function to check the winner
def check_winner(player_hand, dealer_hand, result_label):
    if has_busted(player_hand):
        result_label.configure(text="You busted! Dealer wins.")
    elif has_busted(dealer_hand):
        result_label.configure(text="Dealer busted! You win.")
    elif sum([get_card_value(card[0]) for card in player_hand]) > sum([get_card_value(card[0]) for card in dealer_hand]):
        result_label.configure(text="You win!")
    elif sum([get_card_value(card[0]) for card in player_hand]) < sum([get_card_value(card[0]) for card in dealer_hand]):
        result_label.configure(text="Dealer wins.")
    else:
        result_label.configure(text="It's a tie.")

# Create a function to start a new game
def start_new_game():
    global deck
    # Initialize the deck
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    # Initialize the player's and dealer's hands
    player_hand = []
    dealer_hand = []
    # Deal two cards to the player and dealer
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    # Check for a blackjack
    if is_blackjack(player_hand) and is_blackjack(dealer_hand):
        result_label.configure(text="Both have blackjack. It's a tie.")
    elif is_blackjack(player_hand):
        result_label.configure(text="Blackjack! You win.")
    elif is_blackjack(dealer_hand):
        result_label.configure(text="Dealer has blackjack. Dealer wins.")
    else:
        result_label.configure(text="")
    # Update the card
