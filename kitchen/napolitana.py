from kitchen.pizza import Pizza


class Napolitana(Pizza):

    def __init__(self):
        super().__init__()
    
    def is_delicious(self):
        return True
