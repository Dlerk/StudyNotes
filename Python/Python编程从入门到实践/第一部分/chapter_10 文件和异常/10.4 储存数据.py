# 存储数据
import os,sys
from traceback import print_stack
os.chdir(sys.path[0])

# 使用json储存Python数据结构
import json

numbers = [2, 3, 5, 7, 11, 13]


# `json.dump()` 和 `json.load()`
#   函数json.dump()用于导出数据, 接受两个实参：
#       要存储的数据，以及可用于存储数据的文件对象
#   函数json.load()用于导入数据, 接受一个实参:
#       目标读取json文件

PATH = ".\\data\\numbers.json"
with open(PATH, 'w') as f:
    json.dump(numbers, f)

with open(PATH) as f:
    numbers_2 = json.load(f)

print(numbers_2)


# 保存和读取用户生成的数据

username = input("What is your name? ")

USR_NAME = ".\\data\\usr_name.json"

with open(USR_NAME, 'w') as f:
    json.dump(username, f) 
    print(f"We'll remember you when you come back, {username}!")

with open(USR_NAME) as f:
    usr_name = json.load(f)
    print(f"Welcome back, {username}!")




