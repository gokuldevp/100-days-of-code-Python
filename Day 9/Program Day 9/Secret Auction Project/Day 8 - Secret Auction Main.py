# import os
import auctionart
import random


items_list = {
    "Laptop": 50000,
    "Phone": 15000,
    "Coin": 5000,
    "Crown": 30000000,
    "Car": 8000000,
    "Bike": 600000,
    "Painting": 4000000
}

auction_item_num = random.randint(0,len(items_list)-1)
items = []

for item in items_list:
    items.append(item)

auction_item = items[auction_item_num]
starting_bit = items_list[auction_item]
last_high = starting_bit
next_person = ""
data = {}
again = True

while again == True:

    # if next_person == "yes":
        # os.system('cls')
    print(auctionart.logo)
    print("\nWelcome To Today's online Auction!!!\n")
    print(f"\nThe Item for Today Auction is '{auction_item}'\n")
    print(f"\nThe Starting Bit is '${starting_bit}'\n")
    if last_high > starting_bit:
        print(f"\nThe Highest Bit is '${last_high}'")
    name = input("\nWhat is Your Name?\n").upper()
    bit_amount = int(input("\nWhat is Your Bit Amount?\n$"))
    data[name] = bit_amount
    next_person = input("\nIs There any One else to Bit? Yes or No?\n").lower()

    if bit_amount > starting_bit:
        highest_bit = bit_amount

        if highest_bit > last_high:
            last_high = highest_bit
            highest_bitter = name

        else:
            pass

    else:
        highest_bit = starting_bit

    if next_person == "yes":
        pass

    else:
        again = False

if last_high <= starting_bit:
    print(f"\nSince no one Bit more than Starting Bit: '${starting_bit}', Today's Item '{auction_item}' was Not Auctioned!\n")

else:
    print(f"\n'The Auctioned '{auction_item}' was Won by '{highest_bitter}' for '${last_high}'!\n")

print("\nToday's Auction is Over. So Come again Tomorrow!")
