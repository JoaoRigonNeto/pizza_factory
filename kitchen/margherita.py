from kitchen.pizza import Pizza


class Margherita(Pizza):

    def __init__(self, ingredients):
        super().__init__( ingredients)
    
    def is_delicious(self):
        return True
