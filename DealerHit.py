def dealer_hit():
   global dealer_spot
   if dealer_spot < 5:
      try:
         # Get the player Card
         dealer_card = random.choice(deck)
         # Remove Card From Deck
         deck.remove(dealer_card)
         # Append Card To Dealer List
         dealer.append(dealer_card)
         # Output Card To Screen
         global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5
         
         
         if dealer_spot == 0:
            # Resize Card
            dealer_image1 = resize_cards(f'cards/{dealer_card}.png')
            # Output Card To Screen
            dealer_label_1.config(image=dealer_image1)
            # Increment our player spot counter
            dealer_spot += 1
         elif dealer_spot == 1:
            # Resize Card
            dealer_image2 = resize_cards(f'cards/{dealer_card}.png')
            # Output Card To Screen
            dealer_label_2.config(image=dealer_image2)
            # Increment our player spot counter
            dealer_spot += 1
         elif dealer_spot == 2:
            # Resize Card
            dealer_image3 = resize_cards(f'cards/{dealer_card}.png')
            # Output Card To Screen
            dealer_label_3.config(image=dealer_image3)
            # Increment our player spot counter
            dealer_spot += 1
         elif dealer_spot == 3:
            # Resize Card
            dealer_image4 = resize_cards(f'cards/{dealer_card}.png')
            # Output Card To Screen
            dealer_label_4.config(image=dealer_image4)
            # Increment our player spot counter
            dealer_spot += 1
         elif dealer_spot == 4:
            # Resize Card
            dealer_image5 = resize_cards(f'cards/{dealer_card}.png')
            # Output Card To Screen
            dealer_label_5.config(image=dealer_image5)
            # Increment our player spot counter
            dealer_spot += 1

         # Put number of remaining cards in title bar
         root.title(f'Codemy.com - {len(deck)} Cards Left')

      except:
         root.title(f'CS3250 Card Game - No Cards In Deck')
