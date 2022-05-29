# 继承

# 子类:
#   + 构造函数中调用父类的构造函数
#   + 给子类定义属性和方法
#   +  重写父类方法(虚函数)

class Car:
    """ 一次模拟汽车的简单尝试 """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

"""子类"""
class ElectricCar(Car):
    """ 电动汽车的独特之处 """
    def __init__(self, make, model, year):
        """
        先初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """ 打印一条描述电瓶容量的消息 """
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 将对象用作属性: '包含'

