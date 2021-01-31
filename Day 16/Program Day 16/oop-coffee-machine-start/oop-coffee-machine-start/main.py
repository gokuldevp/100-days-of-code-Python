from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menuitem = MenuItem("name", "water", "milk", "coffee", "cost")
menu = Menu()
create_coffee = CoffeeMaker()
money = MoneyMachine()

on = True

while on:
    order = input(f"What do You want ({menu.get_items()}) :").lower()
    if order == "off":
        on = False
    elif order == "report":
        create_coffee.report()
        money.report()
    else:
        drink = menu.find_drink(order)
        if create_coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                create_coffee.make_coffee(drink)
