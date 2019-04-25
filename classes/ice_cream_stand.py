import restaurant

class IceCreamStand(restaurant.Restaurant):
    """It's an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Inherit the attributes from Restaurant"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("The flavors available at " + self.restaurant_name.title() +
              " are:")
        for flavor in self.flavors:
            print('\t' + flavor)


cold_as_ice = IceCreamStand("cold as ice",
                            "ice cream",
                            ["rocky road", "vanilla", "chocolate"])

cold_as_ice.display_flavors()
