#Sam Schultz
def shuffle():
   # Clear all the old cards from previous games
   dealer_label_1.config(image='')
   dealer_label_2.config(image='')
   dealer_label_3.config(image='')
   dealer_label_4.config(image='')
   dealer_label_5.config(image='')

   player_label_1.config(image='')
   player_label_2.config(image='')
   player_label_3.config(image='')
   player_label_4.config(image='')
   player_label_5.config(image='')


   # Define Our Deck
   suits = ["diamonds", "clubs", "hearts", "spades"]
   values = range(2, 15)
   # 11 = Jack, 12=Queen, 13=King, 14 = Ace

   global deck
   deck =[]

   for suit in suits:
      for value in values:
         deck.append(f'{value}_of_{suit}')

   # Create our players
   global dealer, player, dealer_spot, player_spot
   dealer = []
   player = []
   dealer_spot = 0
   player_spot = 0



   # Shuffle Two Cards for player and dealer
   dealer_hit()
   dealer_hit()

   player_hit()
   player_hit()

   # Put number of remaining cards in title bar
   root.title(f'CS3250 Card Game - {len(deck)} Cards Left')