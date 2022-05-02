# 在Python中，字典一系列键值对每个键都与一个值相关联，
# 你可使用键来访问相关联的值。 

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# 键值对 是两个相关联的值。
# 指定键时，Python将返回与之相关联的值。
# 键和值之间用冒号分隔，而键值对之间用逗号分隔。
# 在字典中，想存储多少个键值对都可以。

# 访问字典中的值
# 要获取与键相关联的值，可依次指定字典名和放在方括号内的键

print(alien_0['color'])

# 添加键值对
# 字典是一种动态结构，可随时在其中添加键值对。
# 要添加键值对，可依次指定字典名、用方括号括起的键和相关联的值。

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 在空字典中添加键值对有时候可提供便利，而有时候必须这样做。
# 为此，可先使用一对空花括号定义一个字典，再分行添加各个键值对。
# 使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时
# 通常需要先定义一个空字典。

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# 删除键值对

del alien_0['points']
print(alien_0)

# 由类似对象组成的字典
# 可以使用字典来存储众多对象的同一种信息

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# 使用get()访问值
# 使用放在方括号内的键从字典中获取感兴趣的值时，可能会引发问题：
# 如果指定的键不存在就会出错
# 可使用方法get() 在指定的键不存在时返回一个默认值
# 从而避免这样的错误。

# 方法get() 的第一个参数用于指定键，是必不可少的；
# 第二个参数为指定的键不存在时要返回的值，是可选的：

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)