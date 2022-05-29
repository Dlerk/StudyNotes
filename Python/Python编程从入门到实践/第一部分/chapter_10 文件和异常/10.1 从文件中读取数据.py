# VSCode bug: 无法识别.py相对路径
# 解决方法:
import os,sys
from traceback import print_stack
os.chdir(sys.path[0])

# 从文件中读取数据

# 读取整个文件
from asyncio import constants

filepath = ".\\data\\pi_digits.txt"

with open(filepath) as file_object:
        contents = file_object.read()
print(contents)

"""分割线"""
print("-----------")

# 逐行读取
# 读取文件时，检查其中的每一行
with open(filepath) as file_object:
    for line in file_object:
            print(line)
            """
            产生更多空白行原因：
            除了文件内的换行符外，
            print()函数也会附加换行符
            """

"""分割线"""
print("-----------")

"""额外换行符解决方法"""
with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())


"""分割线"""
print("-----------")

# 创建包含文件各行内容的列表
with open(filepath) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

"""分割线"""
print("-----------")

# 使用文件的内容

with open(filepath) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
   pi_string += line.strip()

print(pi_string)
print(len(pi_string))

"""
# 注意
# 读取文本文件时,Python将其中的所有文本都解读为字符串
# 如果读取的是数，并要将其作为数值使用
# 就必须使用函数int() 将其转换为整数
# 或使用函数float() 将其转换为浮点数
"""

# 包含大量数据的文件
#   -> 只打印到固定位数

print(f"{pi_string[:12]}...")
print(len(pi_string))

# 检测文件中指定数据


target = input("Enter a numberString, : ")
if target in pi_string:
    print("Target number is in `pi_string`")
else:
     print("Target number is not in `pi_string`")