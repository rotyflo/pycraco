class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a restaurant that sells " +
              self.cuisine_type + ".")


    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open for business!")


restaurant = Restaurant('starbucks', 'coffee')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
