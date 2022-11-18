from kitchen.oven import Oven


first_pizza = Oven.cook_pizza("Peperoni")
print(first_pizza.ingredients)


first_pizza.remove_ingredient("Tomato juice")
print(first_pizza.ingredients)



first_pizza.remove_ingredient("tomato saucE")
print(first_pizza.ingredients)