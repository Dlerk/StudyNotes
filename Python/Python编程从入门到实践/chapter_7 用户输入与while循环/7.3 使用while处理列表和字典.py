# 在列表间移动元素


# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表。
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止。
# 将每个经过验证的用户都移到已验证用户列表中。
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有已验证的用户。
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# 删除为特定值的所有列表元素

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# 使用用户输入来填充字典


responses = {}
# 设置一个标志，指出调查是否继续。
polling_active = True

# 提示输入被调查者的名字和回答。
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

# 将回答存储在字典中。
responses[name] = response

# 看看是否还有人要参与调查。
repeat = input("Would you like to let another person respond? (yes/ no) ")
if repeat == 'no':
    polling_active = False

# 调查结束，显示结果。
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")













