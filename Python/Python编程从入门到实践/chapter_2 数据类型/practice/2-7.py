# 用变量表示一个人的名字，并在其
# 开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"
# 和"\n" 各一次。

name = "\tAda\nlovelace\t"

print(name)

print( name.lstrip() )
print( name.rstrip() )
print( name.strip() )