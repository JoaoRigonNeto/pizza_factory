from kitchen.pizza import Pizza


class Peperoni(Pizza):

    def __init__(self, ingredients):
        super().__init__(ingredients)
    
    def is_delicious(self):
        return True
