import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

proceed = True
bid_list = {}
highest_bidder = ""
highest_price = 0
while proceed:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  next = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  bid_list[name] = price
  # print(bid_list)
  if price > highest_price:
    highest_bidder = name
    highest_price = price
  if next == 'yes':
    os.system('clear')
  else:
    print(f"The winner is {highest_bidder} with a bid of ${bid_list[highest_bidder]}")
    proceed = False
  
  