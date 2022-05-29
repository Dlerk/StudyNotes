# 写入文件

# VSCode bug: 无法识别.py相对路径
# 解决方法:
import os,sys
from traceback import print_stack
os.chdir(sys.path[0])


# 写入空文件
PATH = ".\\data\\output.txt"

with open(PATH, 'w') as file_object:
        file_object.write("Python output file study.")

"""
# 注意：
# Python只能将字符串写入文本文件
# 要将数值数据存储到文本文件中
# 必须先使用函数`str()`将其转换为字符串格式
"""

# 写入多行
# 函数`write()`不会在写入的文本末尾添加换行符
# 要让每个字符串都单独占一行
# 需要在方法调用write() 中包含换行符

with open(PATH, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 给文件附加内容而不是覆盖
#   -> 以附加模式打开文件
# 打开文件时指定了实参'a'
# 以便将内容附加到文件末尾而不是覆盖文件原来的内容

with open(PATH, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")



