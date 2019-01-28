class Restaurant():
	"""Respresent a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes to describe a restaurant."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Print more detailed description of restaurant."""
		print(f"{self.restaurant_name.title()} serves {self.cuisine_type}.")

	def open_restaurant(self):
		"""Print message that restaurant is open."""
		print(f"{self.restaurant_name.title()} is now open!")

	def set_number_served(self, number):
		"""Set the number of customers that have been served."""
		self.number_served = number

	def increment_number_served(self, number):
		"""Increment the number of customers who have been served."""
		self.number_served += number


# restaurant = Restaurant('taco bell', 'mexican-inspired food')
#
# print(restaurant.number_served)
#
# restaurant.number_served = 42
# print(restaurant.number_served)
#
# restaurant.set_number_served(100)
# print(restaurant.number_served)
#
# restaurant.increment_number_served(23)
# print(restaurant.number_served)
