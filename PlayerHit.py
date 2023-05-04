def player_hit():
   global player_spot
   if player_spot < 5:
      try:
         # Get the player Card
         player_card = random.choice(deck)
         # Remove Card From Deck
         deck.remove(player_card)
         # Append Card To Dealer List
         player.append(player_card)
         # Output Card To Screen
         global player_image1, player_image2, player_image3, player_image4, player_image5
         
         
         if player_spot == 0:
            # Resize Card
            player_image1 = resize_cards(f'cards/{player_card}.png')
            # Output Card To Screen
            player_label_1.config(image=player_image1)
            # Increment our player spot counter
            player_spot += 1
         elif player_spot == 1:
            # Resize Card
            player_image2 = resize_cards(f'cards/{player_card}.png')
            # Output Card To Screen
            player_label_2.config(image=player_image2)
            # Increment our player spot counter
            player_spot += 1
         elif player_spot == 2:
            # Resize Card
            player_image3 = resize_cards(f'cards/{player_card}.png')
            # Output Card To Screen
            player_label_3.config(image=player_image3)
            # Increment our player spot counter
            player_spot += 1
         elif player_spot == 3:
            # Resize Card
            player_image4 = resize_cards(f'cards/{player_card}.png')
            # Output Card To Screen
            player_label_4.config(image=player_image4)
            # Increment our player spot counter
            player_spot += 1
         elif player_spot == 4:
            # Resize Card
            player_image5 = resize_cards(f'cards/{player_card}.png')
            # Output Card To Screen
            player_label_5.config(image=player_image5)
            # Increment our player spot counter
            player_spot += 1

         # Put number of remaining cards in title bar
         root.title(f'CS3250 Card Game - {len(deck)} Cards Left')

      except:
         root.title(f'CS3250 Card Game - No Cards In Deck')