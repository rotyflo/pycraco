favorite_pizzas = ['veggie', 'jalapeno', 'cheese']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("pepperoni")
friend_pizzas.append("pineapple")

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
  print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
  print(pizza.title())