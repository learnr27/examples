from demo.car_file import Car, ElectricCar

my_car = ElectricCar('奥迪', 'A9', 2017)
my_car.mod_this_year(2020)
my_car.battery(20)
print(my_car.make)
print(my_car.model)
print(my_car.year)

result = my_car.detection()

print(result)

