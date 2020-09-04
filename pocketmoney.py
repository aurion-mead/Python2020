# Set amount of pocket money
pocket_money = 40.00
still_shopping = True 

#Ask the user for the price of items until they can't afford anymore
while still_shopping == True and pocket_money > 0:
  price = float(input("How much do you want to spend on this item? "))
  
  #Check if they have enough for that item
  if pocket_money - price >= 0:
    pocket_money -= price
  else:
    print("You can't afford that")
    
  print("You have ${:.2f} left".format(pocket_money))
  
  #Check if the user wants to purchase more
  confirm = input("Would you like to keep shopping? ")
  if confirm == "no":
    still_shopping = False
