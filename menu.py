
class MenuItem:
    """Models each Menu Item with optional drizzles."""
    def __init__(self, name, water, milk, coffee, cost, cost1, caramel=0, chocolate=0):
        self.name = name
        self.cost = cost
        self.cost1 = cost1
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
        # Added costs for optional drizzles
        self.caramel = caramel
        self.chocolate = chocolate


class Menu:
    """Models the Menu with drinks and optional drizzles."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5, cost1=3.0),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5, cost1=2.0),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3, cost1=3.5),
            MenuItem(name="americano", water=300, milk=0, coffee=24, cost=2.0,cost1=2.5),
            MenuItem(name="mocha", water=200, milk=150, coffee=24, cost=3.5, cost1=4.0),
            MenuItem(name="macchiato", water=200, milk=100, coffee=24, cost=3.0, cost1=3.5),
            MenuItem(name="flat white", water=200, milk=150, coffee=24, cost=3.0, cost1=3.5),
            MenuItem(name="frappuccino", water=0, milk=300, coffee=24, cost=4.0, cost1=4.5),
            MenuItem(name="chai latte", water=250, milk=100, coffee=0, cost=3.0,cost1=3.5),
            MenuItem(name="matcha latte", water=250, milk=100, coffee=0, cost=3.5, cost1=4.0),
            MenuItem(name="caramel macchiato", water=270, milk=110, coffee=5, cost=4.5, cost1=5.0),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.rstrip('/')

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")





