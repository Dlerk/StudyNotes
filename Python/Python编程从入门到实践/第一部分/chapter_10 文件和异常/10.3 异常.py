# 异常

# 异常是使用`try-except`代码块处理的

# 处理 `ZeroDivisionError` 异常
# 将0作为除数时会引发该异常

from multiprocessing.connection import answer_challenge


try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 使用异常避免崩溃

# else 代码块
# 依赖try 代码块成功执行的代码都应放到else 代码块中

division = input("Input a number as division: ")

try:
    answer=(5/ int(division))
except ZeroDivisionError:
    print("You can't divide by zero!")
else: 
    print(answer)

# `FileNotFoundError` 异常
# 找不到文件：
# 查找的文件可能在其他地方，文件名可能不正确，或者这个文件根本就不存在

# 分析文本

"""" 
spilit()方法:
    它能根据一个字符串创建一个单词`列表`
"""

title = "Alice in Wonderland"
print(title.split())


# 使用多个文件
# 将文件处理改写成方法

# 静默失败: 在expect块中仅填写pass

#   pass 语句还充当了占位符
#   提醒你在程序的某个地方什么都没有做
#   并且以后也许要在这里做些什么

for i in range(2):
    division = input("Input a number as division: ")
    try:
        answer=(5/ int(division))
    except ZeroDivisionError:
        pass
    else: 
        print(answer)








