# 遍历所有键值对

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for k, v in user_0.items():
    print(k+":"+v)

# 如果遍历字典favorite_languages
# 将得到其中每个人的姓名和喜欢的编程语言。
# 因此在循环中使用变量name和language
# 而不是key和value 
# 这让人更容易明白循环的作用

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():  
      print(f"{name.title()}'s favorite language is {language.title()}.")

# 遍历字典中的所有键
# 在不需要使用字典中的值时，方法keys() 很有用

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }   
for name in favorite_languages.keys():
    print(name.title())

# 遍历字典中所有的值

for language in set(favorite_languages.values()):
    print(language.title())

# 通过对包含重复元素的列表调用set()
# 可让Python找出列表中独一无二的元素，并使用这些元素来创建一个集合

