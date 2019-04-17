class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print("Restaurant: " + self.restaurant_name.title())
        print("Cuisine: " + self.cuisine_type)


    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open for business!")


restaurant = Restaurant('starbucks', 'coffee')

print()
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print()
restaurant.describe_restaurant()

print()
restaurant.open_restaurant()
