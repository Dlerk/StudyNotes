# 定义函数

def greet_user():
    """显示简单的问候语。"""
    print("Hello!")

greet_user()


# 位置实参
# 最简单的关联方式是基于实参的顺序，这种关联方式称为位置实参
# 与C/C++格式的函数调用相同

def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')

# 关键字实参
# 关键字实参是传递给函数的名称值对。
# 因为直接在实参中将名称和值关联起来，所以向函数传递实参时不会混淆
# 关键字实参让你无须考虑函数调用中的实参顺序
# 还清楚地指出了函数调用中各个值的用途。

def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

# 默认值
# 编写函数时，可给每个形参指定默认值
# 在调用函数中给形参提供了实参时，Python将使用指定的实参值
# 否则，将使用形参的默认值

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# 











