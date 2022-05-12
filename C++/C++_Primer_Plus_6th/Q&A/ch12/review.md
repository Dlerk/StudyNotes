
# 1.

### Answer:

a. 正确

> 语法正确，但构造函数没有初始化str，应将str指针设置为NULL或使用new[]初始化

b. 不能直接将s赋值给str，因为*str未被分配内存空间

> 构造函数没有创建新的字符串，而只是复制了原有字符串的地址。应当使用new[]和strcpy()

c. 不能对 char* 类型的str应用strcpy()

> 复制了字符串但是没有给他分配储存空间，应该使用new char[len+1]来分配适当数量的空间

#### 注释：

`&emsp;使用char指针时而不是char数组，类声明则不会为字符串本身分配内存空间。必须在构造函数中使用new来为其分配内存空间。这避免了在类声明中预先定义字符串的长度。`

`&emsp;不使用new[]直接将s赋值给str，当s被释放时，str将指向空的地址，引发错误。`

#### 正确代码：

```cpp
class String
{
    char * str;
    int len;

 public:
    String();
    String(const char * s);
    String::Stirng(const String & st);
    ~String();
}

String::String()
{
    len = 0;
    str = new char[1];
    str[0] = '\0';
}

String::String(const char * s)
{
    len = std::strlen(s);
    str = new char[len+1];
    std::strcpy(str,s);
}

String::Stirng(const String & st)
{
    len = st.len;
    str = new char[len+1];
    std::strcpy(str, st.str);
}

String::~String()
{
    delete [] str;
}
 
```

---

# 2

### Answer:

1. 没有为指针成员分配内存就为其赋值 -> 在构造函数中使用new
2. 没有复制传递的参数，而是令指针成员指向了实参的地址 -> 使用深度复制
3. 不知道

> 这种类型的对象过期时，对象的成员指针指向的数据仍将保留在内存中，这将占用空间同时不可访问，因为指针已经丢失 -> 在析构函数中使用delete
> 析构函数释放这种内存后，如果程序将这样的对象初始化为另一个对象，则析构函数将试图释放这些内存两次。这是因为将对象初始化为另一个对象的默认初始化时，将复制指针值而不复制指向的数据，使得两个指针指向相同的数据 -> 定义一个复制构造函数，进行深度复制（使初始化复制指向的数据）
> 一个对象赋值给另一个对象也将导致两个指针指向相同的数据 -> 重载赋值运算符，进行深度复制

`核心思想：复制数据，而不是指针`

---

# 3

### Answer:

+ 默认构造函数
  + 创建一个没有对任何成员初始化的对象
+ 默认复制构造函数
  + 将被复制的对象中的所有成员赋值给接受对象的所有成员
+ 默认赋值运算符
  + 调用复制构造函数
+ 默认析构函数
  + 释放内存

> + 隐式地址运算符：返回调用对象的地址（即this指针的值)

---

# 4

### Answer:

+ personality[]数组未设置大小
+ 默认构造函数中不能令personality初始化为NULL，而是personalitu[0]='\0'
+ 构造函数中，应为strlen(s)+1 ， 且不能直接将s赋值给personality，而应使用strcpy(), talents值为strlen(s)+1
+ 重载<<运算符函数没有返回ostream引用

> 没有将方法设为公有的
> 重载<<运算符函数应为类的友元
> 形参char * s 和 nifty & n 应加const修饰
> 

---

# 5

### Answer:

a.

1. `Glofer()`
2. `Golfer(const char * game, int g=0)`
3. `Golfer(const char * game, int g=0)`
4. `Golfer()`  
5. `Golfer(const Golfer & g)`
6. 类强制类型转换
   > `Golfer(const char * game, int g=0)`
7. 类赋值运算符
8. 类强制类型转换
   > 1. 使用构造函数`Golfer(const char * game, int g=0)`创建一个临时Golfer对象
   > 2. 使用`=`运算符将临时对象的信息复制到nancy对象中
   > 3. 调用析构函数删除临时对象


b. 

深度复制


