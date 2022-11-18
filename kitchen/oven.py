from kitchen.pizza import Pizza
from kitchen.margherita import Margherita
from kitchen.mozzarella import Mozzarella
from kitchen.napolitana import Napolitana
from kitchen.peperoni import Peperoni


class Oven:

    menu = {
            "margherita": Margherita,
            "mozzarella": Mozzarella,
            "napolitana": Napolitana,
            "peperoni": Peperoni
        }

    @classmethod
    def cook_pizza(cls, flavour: str) -> Pizza:
        if flavour.lower() in cls.menu:
            return(cls.menu.get(flavour.lower())())
        else:
            raise ValueError(f"{flavour} not an available flavour")
