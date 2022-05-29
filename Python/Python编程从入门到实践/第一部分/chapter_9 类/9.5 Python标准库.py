# Python标准库

import random

# randint()将两个整数作为参数
# 并随机返回一个位于这两个整数之间（含）的整数
rand = random.randint(1, 6)
print(rand)

# choice()它将一个列表或元组作为参数，并随机返回其中的一个元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = random.choice(players)
print(first_up)