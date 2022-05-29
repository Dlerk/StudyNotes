# 使用类和实例

class Car:
    # 构造函数中形参 'self' 必不可少
    # 而且必须位于其他形参的前面
    def __init__(self, make, model, year):
        """构造函数"""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """返回整洁的描述性信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

#  可以在构造函数内直接给属性指定默认值
class haveDefault:
    def __init__(self, name):
        """构造函数"""
        self.name = name
        self.age = 0

# 修改属性的值:
#   + 直接通过实例进行修改
#   + 通过方法进行设置
#   + 通过方法进行递增


