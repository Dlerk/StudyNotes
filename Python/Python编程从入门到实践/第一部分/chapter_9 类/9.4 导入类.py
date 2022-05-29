# 导入类

# 将 目标类 储存在模块中，使用import语句从导入
# 例如对于储存在`car.py`中的`Car`类

from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 可以在一个模块中储存多个类
# 可以从一个模块中导入多个类
from car import Car, ElectricCar

# 导入整个模块
import car

# 使用别名
from car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())