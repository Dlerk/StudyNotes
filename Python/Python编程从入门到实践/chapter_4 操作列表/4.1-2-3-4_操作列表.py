# 遍历整个列表

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}")

# for 语句末尾的冒号告诉Python，下一行是循环的第一行。

# 创建数值列表
# 函数range() 让Python从指定的第一个值开始数，
# 并在到达你指定的第二个值时停止。因为它在第二个值处停止，所
# 以输出不包含该值（这里为5）。

for value in range(1, 5):
    print(value)

# 使用range()创建数字列表

numbers = list(range(1, 6))

# 对数字列表执行简单的统计运算

min(numbers)
max(numbers)

# 列表解析
# 将循环和创建新元素的代码合成并一行
# 并自动附加新元素

squares = [value**2 for value in range(1, 11)]
print(squares)

# 处理列表的部分元素（切片）
# 你可以生成列表的任意子集。
# 如果没有指定第一个索引，Python将自动从列表开头开始

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 无论列表多长，这种语法都能够让你输出从特定位置到列表末尾的
# 所有元素。
# 上一章说过，负数索引返回离列表末尾相应距离的元素
# 因此你可以输出列表末尾的任意切片。
# 例如，如果要输出名单上的最后三名队员，可使用切片players[-3:] ：

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# Attention :
# 可在表示切片的方括号内指定第三个值。这个值告诉
# Python在指定范围内每隔多少元素提取一个

# 复制列表

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

