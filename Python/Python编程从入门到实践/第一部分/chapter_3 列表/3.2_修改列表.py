# 向列表中添加元素

motor = ['honda','yamaha','suzuki']
print(motor)

motor.append('ducati')
print(motor)

# 在列表中插入元素

motor.insert(0,'tt')
print(motor)

# 从列表中删除元素 

del motor[0]
print(motor)

# 方法pop() 删除列表末尾的元素，并让你能够接着使用它。
# 实际上，可以使用pop() 来删除列表中任意位置的元素，只需在圆
# 括号中指定要删除元素的索引即可。

poped = motor.pop()
print(poped)
print(motor)

# 根据值删除元素

motor.remove('yamaha')
print(motor)