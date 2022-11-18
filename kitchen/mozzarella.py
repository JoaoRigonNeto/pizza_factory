from kitchen.pizza import Pizza


class Mozzarella(Pizza):

    def __init__(self, ingredients):
        super().__init__(ingredients)
    
    def is_delicious(self):
        return True
