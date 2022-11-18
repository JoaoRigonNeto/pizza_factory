from kitchen.pizza import Pizza


class Peperoni(Pizza):

    def __init__(self):
        super().__init__()
    
    def is_delicious(self):
        return True
