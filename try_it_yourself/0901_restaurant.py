class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		return f"{self.restaurant_name.title()} serves {self.cuisine_type}."

	def open_restaurant(self):
		return f"{self.restaurant_name.title()} is now open!"


restaurant = Restaurant('taco bell', 'mexican-inspired food')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
		