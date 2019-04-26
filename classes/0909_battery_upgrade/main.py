from electric_car import ElectricCar

my_car = ElectricCar('cheverolet', 'spark', 2015)

# Range before upgrade
my_car.battery.get_range()

my_car.battery.upgrade_battery()

# Range after upgrade
my_car.battery.get_range()
