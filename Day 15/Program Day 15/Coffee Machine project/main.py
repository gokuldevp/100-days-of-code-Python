# from os import system


LOGO = """

 _____ _________________ _____ _____  ___  ___  ___  _____  _   _ _____ _   _  _____ 
/  __ \  _  |  ___|  ___|  ___|  ___| |  \/  | / _ \/  __ \| | | |_   _| \ | ||  ___|
| /  \/ | | | |_  | |_  | |__ | |__   | .  . |/ /_\ \ /  \/| |_| | | | |  \| || |__  
| |   | | | |  _| |  _| |  __||  __|  | |\/| ||  _  | |    |  _  | | | | . ` ||  __| 
| \__/\ \_/ / |   | |   | |___| |___  | |  | || | | | \__/\| | | |_| |_| |\  || |___ 
 \____/\___/\_|   \_|   \____/\____/  \_|  |_/\_| |_/\____/\_| |_/\___/\_| \_/\____/ 
 
                                                                                                                                                                                                                                                           
"""


MENU = {
    "black coffee": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "strong milk coffee": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "light milk coffee": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """returns report of resources in the system"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"\nwater : {water}ml\nmilk : {milk}ml\ncoffee : {coffee}g\nmoney : ${money}")


def check():
    """return if the resource left is enough for the order"""
    if resources["water"] >= MENU[order]["ingredients"]["water"] and resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
        if "milk" in MENU[order]["ingredients"]:
            if resources["milk"] >= MENU[order]["ingredients"]["milk"]:
                return True
            else:
                print(f"\nLooks like th machine don't have enough resource to {order}")
                return False
        return True
    else:
        print(f"\nLooks like th machine don't have enough resource to {order}")
        return False


def user_money():
    """Return the total amount of money paid by customer"""
    quarters = insert_quarters * 0.25
    dimes = insert_dimes * 0.10
    nickles = insert_nickles * 0.05
    pennies = insert_pennies * 0.01
    total = quarters + dimes + nickles + pennies
    return total


money = 0
on = True
while on:
    print(LOGO)
    order = input("\nwhat would you like? (black coffee, strong milk coffee, light milk coffee) : ").lower()
    if order == "black coffee" or order == "strong milk coffee" or order == "light milk coffee":
        book = check()
        while book:
            print("\nPlease insert coins.")
            insert_quarters = int(input("\nHow many quarters : "))
            insert_dimes = int(input("\nHow many dimes : "))
            insert_nickles = int(input("\nHow many nickles : "))
            insert_pennies = int(input("\nHow many pennies : "))
            user_paid = round(user_money(), 2)
            if user_paid >= MENU[order]["cost"]:
                money += MENU[order]["cost"]
                change = round(user_paid - MENU[order]["cost"], 2)
                print(f"\nHere is Your {order} and your change ${change}.")
                resources["water"] -= MENU[order]["ingredients"]["water"]
                resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
                if "milk" in MENU[order]["ingredients"]:
                    resources["milk"] -= MENU[order]["ingredients"]["milk"]
            else:
                print(f"\n${user_paid} is not enough to buy {order}. You can take the money back.")
            book = False
    elif order == "report":
        report()
    elif order == "off":
        on = False
    else:
        print("\nlooks like you wrote invalid order?")
    enter = input("\nPress 'enter' for next order").lower()
    if enter == "off":
        on = False
    # system("cls")
