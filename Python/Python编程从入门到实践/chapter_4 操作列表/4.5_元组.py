# 元组：不可被修改的列表
# 定义元组:使用圆括号而非中括号来标识

dimensions = (200, 50)

# Attention：
# 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。
# 如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：

my_t = (3,)

# 修改元组变量：虽然不能修改元组的元素，但可以给存储元组的变量赋值。
# 因此，如果要修改元组，可重新定义整个元组：

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
