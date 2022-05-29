# 将函数存储在称为模块的独立文件中
# 再将模块导入到主程序中
# import 语句允许在当前运行的程序文件中使用模块中的代码

# 模块是扩展名为.py的文件，包含要导入到程序中的代码

# 导入特定的函数
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数
# 语法:

from module_name import function_name
from module_name import function_0, function_1, function_

# 使用as给函数和模块指定别名

from pizza import make_pizza as mp
import pizza as p

# 导入模块中的所有函数
# 使用星号（* ）运算符可让Python导入模块中的所有函数

from pizza import *z
