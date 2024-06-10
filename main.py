

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

    if resource_to_top_up in coffee_maker.resources:
        coffee_maker.resources[resource_to_top_up] += amount
    else:
        print("Invalid resource. Please choose from water, milk, or coffee.")


def generate_ascii_table(items):
    headers = ["Name", "Water", "Milk", "Coffee", "Cost", "with Caramel/Chocolate"]
    max_widths = [len(header) for header in headers]

    # Determine the maximum width of each column
    for item in items:
        values = [
            item.name,
            str(item.ingredients["water"]),
            str(item.ingredients["milk"]),
            str(item.ingredients["coffee"]),
            str(item.cost),
            str(item.cost1)
        ]
        for i, value in enumerate(values):
            max_widths[i] = max(max_widths[i], len(value))

    # Create format string for each row
    row_format = "| " + " | ".join([f"{{:<{width}}}" for width in max_widths]) + " |"
    separator = "+-" + "-+-".join(["-" * width for width in max_widths]) + "-+"

    # Build the table
    table = separator + "\n"
    table += row_format.format(*headers) + "\n"
    table += separator + "\n"
    for item in items:
        values = [
            item.name,
            str(item.ingredients["water"]),
            str(item.ingredients["milk"]),
            str(item.ingredients["coffee"]),
            str(item.cost),
            str(item.cost1),
            str(item.caramel),
            str(item.chocolate)
        ]
        table += row_format.format(*values) + "\n"
    table += separator

    return table


# Generate and print the ASCII table
print(generate_ascii_table(menu.menu))

while is_on:
    choice = input(f"What would you like?: ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    elif choice == "supplier":
        supplier(coffee_maker)
    else:
        drink = menu.find_drink(choice)
        if drink:
            caramel = input("Would you like caramel drizzle? (yes/no): ").lower() == "yes"
            chocolate = input("Would you like chocolate drizzle? (yes/no): ").lower() == "yes"

            # Adjusting costs
            if caramel:
                drink.cost += drink.caramel
            if chocolate:
                drink.cost += drink.chocolate

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print("Please enter a valid drink from the given options.")