from number_served import Restaurant

class IceCreamStand(Restaurant):
    """Class representing an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """
        Inherit attributes from Restaurant class,
        then set attribute specific to this class.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def list_flavors(self):
        """List flavors sold at our store."""
        print("Our flavors are:")
        for flavor in self.flavors:
            print('\t' + flavor)

frostys = IceCreamStand(
    "Frostys",
    "ice cream",
    ['chocolate', 'vanilla', 'rocky road', 'cherry', 'peanut butter']
)
frostys.list_flavors()
