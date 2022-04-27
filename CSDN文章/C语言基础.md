<!-- C语言基础 for 期末要考C语言的初学者 -->


本文章仅仅是对课本C语言课程知识的简单梳理以及提供了部分习题练习。另：未涉及指针、结构体、文件处理等知识。

各个知识点的详细内容请前往以下链接进行参照：

* [C语言教程 | runoob](https://www.runoob.com/cprogramming/c-tutorial.html)
* [C语言经典程序 | CSDN](https://www.csdn.net/tags/MtTaEg0sMzc0NzktYmxvZwO0O0OO0O0O.html)
* [C语言中文网](http://c.biancheng.net/c/)

---


# 目录

---

+ [C语言基本程序结构与语法](#1)
+ [基本数据类型](#2)
+ [格式化输入输出与转义字符](#3)
+ [选择与分支结构](#4)
+ [循环](#5)
+ [数组](#6)
+ [函数](#7)
+ [C语言的库函数](#H)
+ [习题汇总](#exc)

---

<br/>

<h1 id='1'>C语言基本程序结构语法 </h1>

本章内容：
+ C语言的程序结构
+ C的基本语法

---

### C语言的程序结构

一个C程序主要包括以下部分：

+ 预处理器指令
+ 函数
+ 变量
+ 语句和表达式
+ 注释

程序清单1.1是一个范例程序：

*程序清单1.1*
```c

#include <stdio.h>  //预处理器指令#include 调用了C标准库 stdio.h
 
int main()  // 程序的主函数，一个可运行的C语言程序中必须有的成分
{

    int a , b ;     // 声明了变量a和b

    a = 1 ;     // 赋值表达式
    b = 2 ;

   /* 这是一段
      跨行注释 */      
   printf("Hello, World! \n");  // 调用stdio.h中的printf函数

   //这是一段单行注释
   
   return 0;    // return 语句返回了0 ，表示程序正常退出
}
```

---

### C的基本语法

#### 分号：

&emsp;在 C 程序中，分号是语句结束符。也就是说，每个语句必须以分号结束。它表明一个逻辑实体的结束。

例如，下面是两个不同的语句：
```c

printf("Hello, World! \n");
return 0;
```

下面的语句虽然跨行，但是仍视作一个语句:
```c

printf("是的，这是仍然被C编译器
       视为同一个语句 \n");
```

#### C语言保留字

&emsp;下表列出了 C 中的保留字。这些保留字不能作为常量名、变量名或其他标识符名称。


|||||||
|:---:|:---:|:---:|:---:|:---:|:---:|
|auto|break|case|char|const|continue|
|default|do|double|else|enum|extern|
|float|for|goto|if|int|long|
|register|return|short|signed|sizeof|static|
|struct|switch|typedef|unsigned|union|void|
volatile|while|

---

<br/>

<h1 id='2'>基本数据类型</h1>

本章内容：
+ 整数类型
+ 浮点类型
+ void类型
+ 指针类型

---

### 整数类型：

|类型|值范围|
|:--:|:--:|
|char|-128~127|
|int|-32,768 ~ 32,767 或 -2,147,483,648 ~ 2,147,483,647|
|short|	0 到 65,535 ~ 或 0 ~ 4,294,967,295|
|long|	-2,147,483,648 ~ 2,147,483,647|

### 浮点类型：

|类型|值范围|精度|
|:--:|:--:|:--:|
|float|	1.2E-38 到 3.4E+38|6位|
|double|	2.3E-308 到 1.7E+308|15位|

### void类型

void 类型指定**没有可用的值**。

---

<br/>

<h1 id='3'>格式化输入输出与转义字符</h1>

本章内容：
+ 格式化输入输出
+ 对字符和字符串的输入输出
+ 转义字符

---

### 格式化输入输出

&emsp;printf()和scanf()函数是C标准库`stdio.h`中的标准输入输出函数。

#### printf()

&emsp;printf() 用于格式化输出到屏幕。

```c
printf(const char *format（格式控制符）, 参数列表);
```

![格式控制符](/CSDN文章/img/printf格式控制符.png)

用法：
```c
    int i = 10;
    int j = 3;
    printf("%d %d\n", i, j);
```
#### scanf()

&emsp;scanf()用于从标准输入流读取输入。

```c
scanf(const char *format（格式控制符）, 参数列表); 
```

> 注：在参数名前需要加取地址运算符`&`

![格式控制符](/CSDN文章/img/scanf%E6%A0%BC%E5%BC%8F%E6%8E%A7%E5%88%B6%E7%AC%A6.png)


用法：
```c
#include <stdio.h>
int main( ) {
 
   char str[100];
   int i;
 
   printf( "Enter a value :");
   scanf("%s %d", str, &i);
 
   printf( "\nYou entered: %s %d ", str, i);
   printf("\n");
   return 0;
}
```

### gechar()与putchar()

&emsp;getchar() 函数从屏幕读取下一个可用的字符，并把它返回为一个整数。这个函数在同一个时间内只会读取一个单一的字符。您可以在循环内使用这个方法，以便从屏幕上读取多个字符。

&emsp;putchar() 函数把字符输出到屏幕上，并返回相同的字符。这个函数在同一个时间内只会输出一个单一的字符。您可以在循环内使用这个方法，以便在屏幕上输出多个字符。

实例:
```c
#include <stdio.h>
 
int main( )
{
   int c;
 
   printf( "Enter a value :");
   c = getchar( );
 
   printf( "\nYou entered: ");
   putchar( c );
   printf( "\n");
   return 0;
}
```
显示如下
> Enter a value :runoob
>
>  You entered: r

### gets() & puts() 函数

&emsp; gets() 函数从 stdin 读取一行到 s 所指向的缓冲区，直到一个终止符或 EOF。

&emsp; puts() 函数把字符串 s 和一个尾随的换行符输出到输出流中。

实例：
```c
#include <stdio.h>
 
int main( )
{
   char str[100];
 
   printf( "Enter a value :");
   gets( str );
 
   printf( "\nYou entered: ");
   puts( str );
   return 0;
}
```

显示如下:
> Enter a value :helloworld
>
> You entered: helloworld

### 转义字符

&emsp;C中定义了一些字母前加"\"来表示常见的那些不能显示的ASCII字符，如\0,\t,\n等，这些称为转义字符，视为单个字符。

转义字符表：
![转义字符](https://bkimg.cdn.bcebos.com/pic/3bf33a87e950352ab1edf5555043fbf2b3118bdb?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U4MA==,g_7,xp_5,yp_5/format,f_auto)

---

# 第一部分 顺序结构习题

[【入门1】 顺序结构](https://www.luogu.com.cn/training/100#problems)

---

<br/>

<h1 id='4'>选择与分支结构</h1>

本章内容：
+ if - else - else if 语句
+ switch语句

---

### if - else - else if 语句

#### if 语句

一个 if 语句 由一个布尔表达式后跟一个或多个语句组成。

```c
if(boolean_expression)
{
   /* 如果布尔表达式为真将执行的语句 */
}
```

#### if - else 语句

一个 if 语句 后可跟一个可选的 else 语句，else 语句在布尔表达式为假时执行。

```c
if(boolean_expression)
{
   /* 如果布尔表达式为真将执行的语句 */
}
else
{
   /* 如果布尔表达式为假将执行的语句 */
}
```

#### if - else if 语句

一个 if 语句 后可跟一个或多个可选的 else if语句。程序将会从第一个if开始判断，当寻找到第一个布尔表达式为真的if时，执行内的代码块。

```c

if(boolean_expression1)
{
    /* 如果布尔表达式为真将执行的语句 */
}
else if(boolean_expression2)
{
    /* 如果第一个if的布尔表达式为假，但此if布尔表达式为真时将执行的语句 */
}

```

### switch语句

一个 switch 语句允许测试一个变量等于多个值时的情况。每个值称为一个 case，且被测试的变量会对每个 switch case 进行检查。

语法：
```c
switch(expression){
    case constant-expression  :
       statement(s);
       break; /* 可选的 */
    case constant-expression  :
       statement(s);
       break; /* 可选的 */
  
    /* 您可以有任意数量的 case 语句 */
    default : /* 可选的 */
       statement(s);
}
```

> 注：没有`break`的话，程序将按顺序执行下方的语句，而不会跳出switch。当所有条件都不满足时，执行default后的语句。

---

# 第二部分 选择与分支结构习题

[【入门2】分支结构](https://www.luogu.com.cn/training/101#problems)

---

<br/>

<h1 id='5'>循环</h1>

本章内容：
+ for循环
+ while循环
+ do whild循环
+ 嵌套循环

---

### for循环

&emsp;for 循环允许您编写一个执行指定次数的循环控制结构。

```c
for ( init; condition; increment )
{
   /*
    循环体
   */;
}
```

---

### while循环

&emsp;只要给定的条件为真，C 语言中的 while 循环语句会重复执行一个目标语句。

```c
while(condition)
{
   /*
    循环体
   */;
}
```

---

### do while循环

&emsp;在 C 语言中，do...while 循环是在循环的尾部检查它的条件。do...while 循环与 while 循环类似，但是 do...while 循环会确保至少执行一次循环。

```c
do
{
   /*
    循环体
   */;
} while( condition );
```

---

### 嵌套循环

&emsp;C 语言允许在一个循环内使用另一个循环。
&emsp;在程序执行过程中，进入外层循环后，程序会在内层循环执行完之后，才会迭代外层循环。

---

# 第三部分 循环结构习题

[【入门3】循环结构](https://www.luogu.com.cn/training/102#problems)

---

<br/>

<h1 id='6'>数组</h1>

本章内容：
+ 声明与初始化数组
+ 多维数组

---

### 声明与初始化数组

在 C 中要声明一个数组，需要指定元素的类型和元素的数量，如下所示：
```c
type arrayName [ arraySize ];
```

对数组的初始化有三种方式:
+ 逐个初始化数组元素
+ 使用初始化语句
+ 使用memset()函数

##### 逐个初始化数组元素

&emsp;即给数组中每个元素赋值。

实例：
```c
int a[3] ;
a[0] = 0 ;
a[1] = 1 ;
a[2] = 2 ;
```

##### 使用初始化语句

&emsp;即在声明时对数组进行初始化

```c
double balance1[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};

//如果您省略掉了数组的大小，数组的大小则为初始化时元素的个数。
double balance2[] = {1000.0, 2.0, 3.4, 7.0, 50.0};
```

##### 使用memset()函数

&emsp;`memset()`函数储存于`string.h`头文件中，是一个初始化函数，作用是将某一块内存中的全部设置为指定的值。

语法：
```c
memset(void *s, int c, size_t n); 
```
+ s指向要填充的内存块。
+ c是要被设置的值。
+ n是要被设置该值的字符数。

实例：
```c
#include <string.h>

int main()
{
   int a[100] ;
   // 将a数组中的所有元素初始化为0
   memset( a, 0 , sizeof(a) ) ;

   return 0 ;
}
```

### 多维数组

多维数组的声明：
```c
type name[size1][size2]...[sizeN];
```

初始化二维数组：
```c
int a[3][4] = {  
 {0, 1, 2, 3} ,   /*  初始化索引号为 0 的行 */
 {4, 5, 6, 7} ,   /*  初始化索引号为 1 的行 */
 {8, 9, 10, 11}   /*  初始化索引号为 2 的行 */
};
```

![二维数组](https://www.runoob.com/wp-content/uploads/2014/09/two_dimensional_arrays.jpg)

内部嵌套的括号是可选的，下面的初始化与上面是等同的：
```c
int a[3][4] = {0,1,2,3,4,5,6,7,8,9,10,11};
```

---

# 第四部分 数组习题

[【入门4】数组](https://www.luogu.com.cn/training/103#problems)

---

<br>

<h1 id='7'>函数</h1>

本章内容：
+ 函数声明
+ 形参与实参
+ 传参方式

---

### 函数声明

C 语言中的函数定义的一般形式如下：

```c
return_type function_name( parameter list )
{
   body of the function
}
```

&emsp;在 C 语言中，函数由一个函数头和一个函数主体组成。下面列出一个函数的所有组成部分：

+ **返回类型**：一个函数可以返回一个值。return_type 是函数返回的值的数据类型。有些函数执行所需的操作而不返回值，在这种情况下，return_type 是关键字 void。
+ **函数名称**：这是函数的实际名称。函数名和参数列表一起构成了函数签名。
+ **参数**：参数就像是占位符。当函数被调用时，您向参数传递一个值，这个值被称为实际参数。参数列表包括函数参数的类型、顺序、数量。参数是可选的，也就是说，函数可能不包含参数。
+ **函数主体**：函数主体包含一组定义函数执行任务的语句。

---

### 形参与实参

+ **形参（形式参数）**
&emsp;在函数定义中出现的参数可以看做是一个占位符，它没有数据，只能等到函数被调用时接收传递进来的数据，所以称为形式参数，简称形参。
+ **实参（实际参数）**
&emsp;函数被调用时给出的参数包含了实实在在的数据，会被函数内部的代码使用，所以称为实际参数，简称实参。

&emsp;形参和实参的功能是传递数据，发生函数调用时，实参的值会传递给形参。

请看以下实例：
```c
#include <stdio.h>

//计算从m加到n的值
int sum(int m, int n) {
    int i;
    for (i = m+1; i <= n; ++i) {
        m += i;
    }
    return m;
}

int main() {
    int a, b, total;
    printf("Input two numbers: ");
    scanf("%d %d", &a, &b);
    total = sum(a, b);
    printf("a=%d, b=%d\n", a, b);
    printf("total=%d\n", total);

    return 0;
}
```
运行结果：
> 运行结果：
Input two numbers: 1 100
a=1, b=100
total=5050

&emsp;在这段代码中，函数定义处的 m、n 是形参，函数调用处的 a、b 是实参。通过 scanf() 可以读取用户输入的数据，并赋值给 a、b，在调用 sum() 函数时，这份数据会传递给形参 m、n。

&emsp;从运行情况看，输入 a 值为 1，即实参 a 的值为 1，把这个值传递给函数 sum() 后，形参 m 的初始值也为 1，在函数执行过程中，形参 m 的值变为 5050。函数运行结束后，输出实参 a 的值仍为 1，可见实参的值不会随形参的变化而变化。

---

### 传参方式

当调用函数时，有两种向函数传递参数的方式：

|调用类型|描述|
|:-:|:-:|
|[传值调用](https://www.runoob.com/cprogramming/c-function-call-by-value.html)|该方法把参数的实际值复制给函数的形式参数。在这种情况下，修改函数内的形式参数不会影响实际参数。|
|[传引用调用](https://www.runoob.com/cprogramming/c-function-call-by-pointer.html)|通过指针传递方式，形参为指向实参地址的指针，当对形参的指向操作时，就相当于对实参本身进行的操作。|

---

# 第五部分：字符串习题

[【入门5】字符串](https://www.luogu.com.cn/training/104#problems)


# 第六部分：函数习题

[【入门6】函数与结构体](https://www.luogu.com.cn/training/105#problems)

---

<h1 id='H'>C的常用库</h1>

本章内容：

&emsp;C语言中常用的库（头文件）以及对应的常用函数。

> 点击对应函数可跳转到其定义与用法。

---

### `<stdio.h>`:

+ [`printf(const char *format, ...)`](https://www.runoob.com/cprogramming/c-function-printf.html) 发送格式化输出到标准输出 stdout。
+ [`scanf(const char *format, ...)`](https://www.runoob.com/cprogramming/c-function-scanf.html) 从标准输入 stdin 读取格式化输入。
+ [`sscanf(const char *str, const char *format, ...) `](https://www.runoob.com/cprogramming/c-function-sscanf.html) 从字符串读取格式化输入。
+ [`getchar(void)`](https://www.runoob.com/cprogramming/c-function-getchar.html) 从标准输入 stdin 获取一个字符（一个无符号字符）。
+ [`gets(char *str)`](https://www.runoob.com/cprogramming/c-function-gets.html) 从标准输入 stdin 读取一行，并把它存储在 str 所指向的字符串中。当读取到换行符时，或者到达文件末尾时，它会停止，具体视情况而定。
+ [`putchar(int char)`](https://www.runoob.com/cprogramming/c-function-putchar.html) 把参数 char 指定的字符（一个无符号字符）写入到标准输出 stdout 中。
+ [`puts(const char *str)`](https://www.runoob.com/cprogramming/c-function-puts.html) 把一个字符串写入到标准输出 stdout，直到空字符，但不包括空字符。换行符会被追加到输出中。

### `<ctype.h>`:

+ [`isalpha(int c)`](https://www.runoob.com/cprogramming/c-function-isalpha.html) 该函数检查所传的字符是否是字母。
+ [`isdigit(int c)`](https://www.runoob.com/cprogramming/c-function-isdigit.html) 该函数检查所传的字符是否是十进制数字。
+ [`islower(int c)`](https://www.runoob.com/cprogramming/c-function-islower.html) 该函数检查所传的字符是否是小写字母。
+ [`isupper(int c)`](https://www.runoob.com/cprogramming/c-function-isupper.html) 该函数检查所传的字符是否是大写字母

### `<math.h>`:

+ [`pow(double x, double y)`](https://www.runoob.com/cprogramming/c-function-pow.html) 返回 x 的 y 次幂。
+ [`sqrt(double x)`](https://www.runoob.com/cprogramming/c-function-sqrt.html) 返回 x 的平方根。
+ [`double fabs(double x)`](https://www.runoob.com/cprogramming/c-function-fabs.html) 返回 x 的绝对值。

### `<string.h>`:

+ [`strcat(char *dest, const char *src)`](https://www.runoob.com/cprogramming/c-function-strcat.html) 把 src 所指向的字符串追加到 dest 所指向的字符串的结尾。
+ [`strchr(const char *str, int c)`](https://www.runoob.com/cprogramming/c-function-strchr.html) 在参数 str 所指向的字符串中搜索第一次出现字符 c（一个无符号字符）的位置。
+ [`strncmp(const char *str1, const char *str2, size_t n)`](https://www.runoob.com/cprogramming/c-function-strcmp.html) 把 str1 和 str2 进行比较，最多比较前 n 个字节。
+ [`strcpy(char *dest, const char *src)`](https://www.runoob.com/cprogramming/c-function-strcpy.html)把 src 所指向的字符串复制到 dest。
+ [`strlen(const char *str)`](https://www.runoob.com/cprogramming/c-function-strlen.html) 计算字符串 str 的长度，直到空结束字符，但不包括空结束字符。
+ [`strstr(const char *haystack, const char *needle)`](https://www.runoob.com/cprogramming/c-function-strstr.html) 在字符串 haystack 中查找第一次出现字符串 needle（不包含空结束字符）的位置。

### `<stdlib.h>`:

+ [`atoi(const char *str)`](https://www.runoob.com/cprogramming/c-function-atoi.html) 把参数 str 所指向的字符串转换为一个整数（类型为 int 型）。
+ [`abs(int x)`](https://www.runoob.com/cprogramming/c-function-abs.html) 返回 x 的绝对值
+ [`qsort(void *base, size_t nitems, size_t size, int (*compar)(const void *, const void*))`](https://www.runoob.com/cprogramming/c-function-qsort.html) 快速排序算法。

---

# 习题汇总

[【入门1】 顺序结构](https://www.luogu.com.cn/training/100#problems)
[【入门2】分支结构](https://www.luogu.com.cn/training/101#problems)
[【入门3】循环结构](https://www.luogu.com.cn/training/102#problems)
[【入门4】数组](https://www.luogu.com.cn/training/103#problems)
[【入门5】字符串](https://www.luogu.com.cn/training/104#problems)
[【入门6】函数与结构体](https://www.luogu.com.cn/training/105#problems)


#### 进阶：枚举算法练习：

[【算法1-3】暴力枚举](https://www.luogu.com.cn/training/108#problems)

---

##### 参考资料

[菜鸟教程|runoob](https://www.runoob.com/cprogramming/c-tutorial.html)
[C语言中文网](http://c.biancheng.net/c/)
[洛谷](https://www.luogu.com.cn/)
[CSDN](https://www.csdn.net/)
C Primer Plus （第6版）中文版 / （美）史蒂芬·普拉达(Stephen Prata)著.北京:人民邮电出版社,2019.11