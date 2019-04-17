class Restaurant():
    """Let's build a restaurant!"""

    def __init__(self, restaurant_name, cuisine_type):
        """Inititialize the Restaurant class."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print out a description of the restaurant."""
        print(self.restaurant_name.title() + " is a restaurant that sells " +
              self.cuisine_type + ".")

    def open_restaurant(self):
        """Tell user that the restaurant is now open."""
        print(self.restaurant_name.title() + " is open for business!")

    def set_number_served(self, value):
        """Set the amount of customers who have been served."""
        self.number_served = value

    def increment_number_served(self, value):
        """Increase the number of customers served by a given amount."""
        self.number_served += value


restaurant = Restaurant('starbucks', 'coffee')

print(restaurant.number_served)

restaurant.number_served += 1
print(restaurant.number_served)

restaurant.set_number_served(10)
print(restaurant.number_served)

restaurant.increment_number_served(100)
print(restaurant.number_served)
