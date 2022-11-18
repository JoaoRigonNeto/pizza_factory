from kitchen.oven import Oven


print("WELCOME TO BIBIS PIZZARIA")

bibi_special_pizza = Oven.cook_pizza(flavour = "Margherita")
print(bibi_special_pizza)
bibi_special_pizza.remove_ingredient("ToMaTo")
bibi_special_pizza.remove_ingredient("ToMaTo")

bibi_special_pizza.add_ingredient("bibi`s special sauce")
bibi_special_pizza.add_ingredient("bibi`s special sauce")
bibi_special_pizza.add_ingredient("bibi`s special sauce")
bibi_special_pizza.add_ingredient("bibi`s special sauce")
bibi_special_pizza.add_ingredient("bibi`s special sauce")

print(bibi_special_pizza.basic_ingredients)
