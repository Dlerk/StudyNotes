<h1 id='chapter12'>第十四章 C++中的代码重用</h1>

<div class="chapterContent">
<br/>

&emsp;**本章内容:**

  <span class="chapterContent_">

  + has-a 关系
  + 包含对象成员的类
  + 模板类valarray
  + 私有保护继承
  + 多重继承
  + 虚基类
  + 创建类模板
  + 使用类模板
  + 模板的具体化

  </span>

<br/>
</div>

---

### 包含*对象* 成员的类

#### 建立 has-a 关系

+ 组合（包含）技术

  即创建一个包含其他类对象的类。
  例如：
  ```cpp
  class student
  {
    private:
      string name;
      valarray<double> source;
      ···
  }
  ```
  &emsp;这意味着student类的成员函数可以使用string和valarray类的共有借口来访问和修改name和scores对象。


*接口和实现*

> &emsp;使用公有继承时，类可以集成接口，可能还有实现(基类的纯虚函数提供接口但不提供实现)。
> 获得接口是is-a的组成部分。而使用组合，类可以获得实现而不能获得接口。
> 不继承接口是has-a关系的组成部分。







---

### `valarray` 类

&emsp; valarray类是由头文件`valarray`支持的。

该类用于处理数值.支持诸如将数组中所有元素的值相加以及在数组中找出最大和最小值等操作。是一个`模板类`。

*定义:*
```cpp
valarray<typename> arrayname ;
// valarray数组支持初始化
valarray<typename> arrayname = {10,8} ;
```

下面是这个类的一些方法

> + operator[](): 访问元素
> + size(): 返回包含的元素数
> + sum(): 返回所有元素的总和
> + max(): 返回最大元素
> + min(): 返回最小元素










---










