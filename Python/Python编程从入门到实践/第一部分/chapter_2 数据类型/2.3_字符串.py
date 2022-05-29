# 方法title()以首字母大写的方式显示每个单词,title不需要参数

name = "ada lovelace"
print( name.title() )

# 方法lower()将字符串改为全部小写
# 方法upper()将字符串改为全部大写

name = "Ada Lovelace"
print( name.lower() )
print( name.upper() )
 
# 在字符串中使用变量，要在字符串中插入变量的值，
# 可在前引号前加上字母f，再将要插入的变量放在花括号内。
# 这种字符串名为f字符串 。f是format（设置格式）的简写，因为Python
# 通过把花括号内的变量替换为其值来设置字符串的格式。

f_name = "ada"
l_name = "lovelace"
full_name = f"{f_name} {l_name}"
print(full_name)
print(f"Hello,{full_name.title()}!")

# 添加空白

print("Python")
print("\tPython!")

# 删除空白
# rstrip()方法删除字符串末尾的空白
# lstrip()方法删除字符串前端的空白
# strip()方法删除两端的空白

msg = " python "
print(msg)
print(msg.strip())






