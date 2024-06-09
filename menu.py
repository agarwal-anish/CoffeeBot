# class MenuItem:
#     """Models each Menu Item."""
#     def __init__(self, name, water, milk, coffee, cost):
#         self.name = name
#         self.cost = cost
#         self.ingredients = {
#             "water": water,
#             "milk": milk,
#             "coffee": coffee
#         }
#
#
# class Menu:
#     """Models the Menu with drinks."""
#     def __init__(self):
#         self.menu = [
#             MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
#             MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
#             MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
#         ]
#
#     def get_items(self):
#         """Returns all the names of the available menu items"""
#         options = ""
#         for item in self.menu:
#             options += f"{item.name}/"
#         return options
#
#     def find_drink(self, order_name):
#         """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
#         for item in self.menu:
#             if item.name == order_name:
#                 return item
#         print("Sorry that item is not available.")






class MenuItem:
    """Models each Menu Item with optional drizzles."""
    def __init__(self, name, water, milk, coffee, cost, caramel=0, chocolate=0):
        self.name = name
        self.cost = cost
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
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3, caramel=0.5, chocolate=0.5),
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
