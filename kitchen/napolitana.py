from kitchen.pizza import Pizza


class Napolitana(Pizza):

    def __init__(self):
        super().__init__()
        self.ingredients = ["tomato sauce", "mozzarella cheese", "basil"]
    
    def is_delicious(self):
        return True

    def remove_ingredient(self, ingredient: str):
        if ingredient.lower() in self.ingredients:
            self.ingredients.remove(ingredient.lower())
        