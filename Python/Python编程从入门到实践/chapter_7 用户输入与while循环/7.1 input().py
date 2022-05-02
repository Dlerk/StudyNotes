# 函数input() 让程序暂停运行，等待用户输入一些文本。
# 函数input() 接受一个参数——
# 要向用户显示的提示或说明，让用户知道该如何做
# 使用函数input() 时，Python将用户输入解读为字符串。

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 有时候，提示可能超过一行。
# 在这种情况下，可将提示赋给一个变量，再将该变量传递给函数input()

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# 使用int()获取数值输入

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# 取模运算符：%










