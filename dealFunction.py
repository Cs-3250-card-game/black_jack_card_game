from tkinter import *
import random
from PIL import Image, ImageTk
import os

#Code found from the following tutorial on YouTube by Codemy.com: https://www.youtube.com/watch?v=gBS2pYAGUgA

root = Tk()
root.title('CS3250 Card Game - Card Deck')
root.geometry("1200x800")
root.configure(background="green")

def deal_cards():
   try:
      # Get the deler Card
      card = random.choice(deck)
      # Remove Card From Deck
      deck.remove(card)
      # Append Card To Dealer List
      dealer.append(card)
      # Output Card To Screen
      global dealer_image
      dealer_image = resize_cards(f'cards/{card}.png')
      dealer_label.config(image=dealer_image)
      #dealer_label.config(text=card)

      # Get the player Card
      card = random.choice(deck)
      # Remove Card From Deck
      deck.remove(card)
      # Append Card To Dealer List
      player.append(card)
      # Output Card To Screen
      global player_image
      player_image = resize_cards(f'cards/{card}.png')
      player_label.config(image=player_image)
      #player_label.config(text=card)


      # Put number of remaining cards in title bar
      root.title(f'CS3250 Card Game - {len(deck)} Cards Left')

   except:
      root.title(f'CS3250 Card Game - No Cards In Deck')
