from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


def supplier(resource):
    resource_to_top_up = input("What would you like to top up? (water/milk/coffee): ").lower()
    amount = int(input(f"How much {resource_to_top_up} would you like to add? "))

    if resource_to_top_up == "water":
        coffee_maker.resources['water'] += amount
    elif resource_to_top_up == "milk":
        coffee_maker.resources['milk'] += amount
    elif resource_to_top_up == "coffee":
        coffee_maker.resources['coffee'] += amount
    else:
        print("Invalid resource. Please choose from water, milk, or coffee.")


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) or (supplier/report/off): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    elif choice == "supplier":
        supplier(coffee_maker)
    elif choice in ["latte", "espresso", "cappuccino"]:
        drink = menu.find_drink(choice)
        if drink:
            # Asking for customization
            caramel = input("Would you like caramel drizzle? (yes/no): ").lower() == "yes"
            chocolate = input("Would you like chocolate drizzle? (yes/no): ").lower() == "yes"

            # Adjusting costs
            if caramel:
                drink.cost += drink.caramel
            if chocolate:
                drink.cost += drink.chocolate

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                if caramel:
                    print("Adding caramel drizzle...")
                if chocolate:
                    print("Adding chocolate drizzle...")
                print(f"Here is your {drink.name} ☕️. Enjoy!")
    else:
        print("Please enter a valid drink from the given options.")


