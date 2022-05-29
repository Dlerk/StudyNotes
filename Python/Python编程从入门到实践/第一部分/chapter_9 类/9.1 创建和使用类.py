# 创建与使用类

class Dog:
    # 构造函数中形参 'self' 必不可少
    # 而且必须位于其他形参的前面
    def __init__(self, name, age):
        """构造函数"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()