class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		return f"{self.restaurant_name.title()} serves {self.cuisine_type}."

	def open_restaurant(self):
		return f"{self.restaurant_name.title()} is now open!"


restaurant_0 = Restaurant('taco bell', 'mexican-inspired food')
restaurant_1 = Restaurant('burger king', 'burgers')
restaurant_2 = Restaurant('starbucks', 'coffee')

print(restaurant_0.describe_restaurant())
print(restaurant_1.describe_restaurant())
print(restaurant_2.describe_restaurant())