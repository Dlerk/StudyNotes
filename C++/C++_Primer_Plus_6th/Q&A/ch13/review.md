
# 1

公有成员和保护成员

> 基类的公有成为派生类的公有，基类的保护成为派生类的保护。基类的私有成员被继承，但是不能直接访问。

# 2

私有成员
> 不能继承构造函数、析构函数、赋值运算符和友元

# 3

不能连续使用赋值运算符。创建新的临时变量，占用内存空间。

> 仍可以单个复制，但不能连锁赋值。方法的执行速度减慢，因为返回语句需要复制对象。

# 4

先调用基类构造函数，再调用派生类构造函数
先调用派生类析构函数，再调用基类析构函数

> 按派生的顺序调用构造函数，FIFO。析构函数，FILO。

# 5

需要。必须使用构造函数，对象才能被创建。

> 每个类都必须有自己的构造函数

# 6

派生类的方法。

> 只调用派生类方法，它取代基类定义。仅当派生类没有重新定义方法或者使用域解析运算符时，才会调用基类方法。应该把所有要重新定义的函数声明为虚函数。

# 7

不知道

> 如果派生类构造函数使用new来初始化类的成员指针，则应定义一个赋值运算符。
> 普遍地将，如果对于派生类成员来说，默认赋值不正确，则应定义赋值运算符。

# 8

可以。不可以。
向下兼容规则。

> 可以将派生类对象的地址赋给基类指针
> 只有通过显式类型转换，才可以将基类对象的地址赋给派生类指针，而使用这样的指针不一定安全

# 9

可以，不可以。

> 可以将派生类对象赋给基类对象，派生类中新增的数据成员都不会传递给基类对象。程序将使用基类的赋值运算符。
> 仅当派生类定义了转换运算符，或者使用基类为参数的赋值运算符时，才能将基类赋值给派生类。

# 10

基类指针和引用既可以指向基类，也可以指向其派生类。

# 11

同上。

> 按值传递对象将调用复制构造函数。由于形参是基类对象，因此将调用基类的复制构造函数。
> 复制构造函数以基类为引用作为参数，该引用可以参数传递的派生对象。
> 最终结果：将生成一个新的基类对象，其成员对应于派生对象的基类部分。

# 12

按值传递对象会将原对象复制，创建一个临时对象，占用额外的内存和系统操作。

> 按引用传递对象，可以确保函数从虚函数受益。
> 按引用传递对象，可以节省内存和时间。

# 13

a. 调用哪个head()方法取决于ph的类型
b. 调用哪个head()方法取决于ph所指向对象的类型

> 如果head()是一个常规方法，ph->head()将调用基类的方法;如果head()是虚函数，ph->head()将调用派生类的方法。

# 14

+ 基类中虚方法存在定义
+ 没有对all_sq_ft初始化，就在构造函数中对其使用算术运算符
+ House访问了基类Kitchen 的私有对象
+ 两者的关系出错：应为House `hsa` Kitchen

> 情况不符合is-a模型，公有继承不适用
> House中的area()定义隐藏了area()的Kitchen版本






