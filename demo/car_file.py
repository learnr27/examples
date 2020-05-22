class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.this_year = 2018

    def mod_this_year(self, new_year):
        self.this_year = new_year

    def detection(self):
        duration = self.this_year - self.year
        price = 30 - 2 * duration
        long_name = "你的" + self.make + self.model + "到目前已经行驶了" + str(duration) + "年,目前价值" + str(price) + "万"
        return long_name


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def battery(self, capacity):
        self.capacity_num = capacity
        print('您的电池容量为：', self.capacity_num, 'kWh')

    def detection(self):
        duration = self.this_year - self.year
        price = 30 - duration - (500 / self.capacity_num)
        long_name = "1你的" + self.make + self.model + "到目前已经行驶了" + str(duration) + "年,目前价值" + str(price) + "万"
        return long_name
