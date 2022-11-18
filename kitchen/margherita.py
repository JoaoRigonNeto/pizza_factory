from kitchen.pizza import Pizza


class Margherita(Pizza):

    def __init__(self):
        super().__init__()
        self.ingredients = ["tomato sauce", "mozzarella cheese", "parmegiano-reggiano cheese", "basil", "red pepper"]
    
    def is_delicious(self):
        return True

    def remove_ingredient(self, ingredient: str):
        if ingredient.lower() in self.ingredients:
            self.ingredients.remove(ingredient.lower())