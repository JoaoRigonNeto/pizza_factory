from kitchen.pizza import Pizza


class Margherita(Pizza):

    def __init__(self):
        super().__init__()
        self.basic_ingredients = ["cheese", "tomato", "bibi`s special sauce"]
        self.removable_ingredients = ["tomato"]
        self.addable_ingredients = ["bibi`s special sauce"]
    
    def is_delicious(self):
        return True

    def remove_ingredient(self, ingredient: str):
        if ingredient.lower() in self.basic_ingredients and ingredient.lower() in self.removable_ingredients:
            self.basic_ingredients.remove(ingredient.lower())
        
    def add_ingredient(self, ingredient: str):
        if ingredient.lower() in self.basic_ingredients and ingredient.lower() in self.addable_ingredients:
            self.basic_ingredients.append(ingredient.lower())