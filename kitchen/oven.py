from kitchen.pizza import Pizza
from kitchen.margherita import Margherita
from kitchen.mozzarella import Mozzarella
from kitchen.napolitana import Napolitana
from kitchen.peperoni import Peperoni

menu = {
        "margherita": Margherita,
        "mozzarella": Mozzarella,
        "napolitana": Napolitana,
        "peperoni": Peperoni
    }

class Oven:

    @staticmethod
    def cook_pizza(flavour: str, ingredients: list) -> Pizza:
        return menu.get(flavour.lower(), None)(ingredients)
