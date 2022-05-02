# while循环则不断运行，直到指定的条件不满足为止

# 在要求很多条件都满足才继续运行的程序中，可定义一个变量
# 用于判断整个程序是否处于活动状态
# 这个变量称为标志 （flag），充当程序的交通信号灯

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# 使用break退出循环
# 在循环中使用continue使循环迭代





