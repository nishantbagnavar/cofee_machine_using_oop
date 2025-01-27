from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()


is_on = True
while is_on:
    order_name = input(f"What would you like to drink? {my_menu.get_items()}: ").lower()

    if order_name=="report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif order_name=="off":
        is_on=False

    else:
        drink = my_menu.find_drink(order_name)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)