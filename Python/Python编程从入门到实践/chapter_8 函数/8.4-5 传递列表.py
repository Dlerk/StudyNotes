# 将列表传递给函数后，函数就能直接访问其内容


def greet_users(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 在函数中修改列表
# 将列表传递给函数后，函数就可对其进行修改
# 在函数中对这个列表所做的任何修改都是永久性的

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
        completed_models = []

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 禁止函数修改列表
# 向函数传递列表的副本而非原件
# 切片表示法[:] 创建列表的副本
# 语法： function_name(list_name_[:])

print_models(unprinted_designs[:], completed_models)

# 传递任意数量的实参
# 有时候，预先不知道函数需要接受多少个实参
# 好在Python允许函数从调用语句中收集任意数量的实参
# 下面的函数只有一个形参*toppings
# 但不管调用语句提供了多少实参，这个形参会将它们统统收入囊中

def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参
# 必须在函数定义中将接纳任意数量实参的形参放在最后

def make_pizza(size, *toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参
# 需要接受任意数量的实参
# 但预先不知道传递给函数的会是什么样的信息
# 可将函数编写成能够接受任意数量的键值对:
# 调用语句提供了多少就接受多少

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)

# 形参**user_info 中的两个星号让Python创建一个名为user_info 的空字典
# 并将收到的所有名称值对都放到这个字典中










