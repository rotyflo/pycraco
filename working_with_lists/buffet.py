buffet_foods = ('pizza', 'chicken nuggets', 'pasta', 'brownies', 'rolls')

print("Original buffet menu:")
for food in buffet_foods:
	print(food.title())

# CAN'T MODIFY INDIVIDUAL ITEMS IN TUPLES
#buffet_foods[2] = 'jelly'

buffet_foods = ('pizza', 'chicken nuggets', 'jelly', 'brownies', 'tacos')

print("\nNew buffet menu:")
for food in buffet_foods:
	print(food.title())