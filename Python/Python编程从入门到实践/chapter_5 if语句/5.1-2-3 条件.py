# 简单示例

from doctest import FAIL_FAST


cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 条件检查时对大小写敏感

# 检查多个条件
# and:与
# or:或

age_0 = 22
age_1 = 18

if( age_0>=21 and age_1>=21 ):
    print(True)
else:
    print(False)

# 检查特定值是否在列表中或是否不在列表中

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if "mushrooms" in requested_toppings :
    print('Yes')
else:
    print('No')

if "Apple" not in requested_toppings :
    print("Yes")

# if-elif-if 语句

age = 12 
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")






