<!-- CSS Study Progress -->

目录
---

+ [CSS简介](#chapter0)
+ [CSS语法](#chapter1)
+ [CSS使用](#chapter2)
+ [CSS基础应用](#chapter3)







---

<br/>
<br/>
<br/>

<h1 id='chapter0'>CSS简介</h1>

-----

### 什么是CSS？
+ CSS 指的是层叠样式表* (Cascading Style Sheets)
  ` *也称级联样式表 `
+ CSS 描述了如何在屏幕、纸张或其他媒体上显示 HTML 元素
+ CSS 节省了大量工作。它可以同时控制多张网页的布局
+ 外部样式表存储在 CSS 文件中

---

### 外部样式表
+ 样式定义通常保存在外部 .css 文件中
+ 通过使用外部样式表文件，只需更改一个文件即可更改整个网站的外观

---

<br/>

<h1 id='chapter1'>一、CSS语法</h1>

本章内容由以下组成

* [CSS规则集](#css规则集)
* [CSS选择器](#css选择器)
* [CSS注释](#css-注释)


---

### CSS规则集
  
由选择器和声明块组成：
  ![rule-set](https://www.w3school.com.cn/i/css/selector.gif)

+ 选择器：指向您需要设置样式的 HTML 元素。
+ 声明块：包含一条或多条用分号分隔的声明。

&emsp;每条声明都包含一个 CSS 属性名称和一个值，以冒号分隔。

&emsp;多条 CSS 声明用分号分隔，声明块用花括号括起来。

---

### CSS选择器

CSS 选择器用于“查找”（或选取）要设置样式的 HTML 元素。

我们可以将 CSS 选择器分为五类：

  * 简单选择器（根据名称、id、类来选取元素）
  * 组合器选择器（根据它们之间的特定关系来选取元素）
  * 伪类选择器（根据特定状态选取元素）
  * 伪元素选择器（选取元素的一部分并设置其样式）
  * 属性选择器（根据属性或属性值来选取元素）

##### CSS 元素选择器

&emsp;元素选择器根据元素名称选择HTML函数。

```css

p {
  text-align: center;
  color: red;
}

```

##### CSS id选择器

&emsp;id选择器使用HTML元素的id属性来选择特定元素。

> 元素的 id 在页面中是唯一的，因此 id 选择器用于选择一个唯一的元素

要选择具有特定 id 的元素，请写一个井号（＃），后跟该元素的 id。

```css

#para1 {
  text-align: center;
  color: red;
}

```

`注意：id 名称不能以数字开头。`

##### CSS 类选择器

&emsp;类选择器选择有特定 class 属性的 HTML 元素。

如需选择拥有特定 class 的元素，请写一个句点（.）字符，后面跟类名。

```css

/* 在此例中
   所有带有 class="center" 的 HTML 元素
   将为红色且居中对齐 */
.center {
  text-align: center;
  color: red;
}

/* 在这个例子中
   只有具有 class="center" 的 <p> 元素会居中对齐： */
p.center {
  text-align: center;
  color: red;
}

```

HTML 元素也可以引用多个类。

```css

/* 在这个例子中
   <p> 元素将根据 class="center" 
   和 class="large" 进行样式设置 */

<p class="center large">这个段落引用两个类。</p>

```

##### CSS 通用选择器

&emsp; 通用选择器（*）选择页面上的所有的 HTML 元素。

```css

* {
  text-align: center;
  color: blue;
}

```

##### CSS 分组选择器

&emsp;分组选择器选取所有具有相同样式定义的 HTML 元素。

```css

h1, h2, p {
  text-align: center;
  color: red;
}

```

---

### CSS 注释

```css

/* 这是一条单行注释 */

/* 这是
一条多行的
注释 */ 

<!-- 这是一行HTML注释 -->

```

---

<br/>



<h1 id='chapter2'>二、CSS使用</h1>

本章内容：
+ [使用CSS的方法]
+ [层叠顺序]

---

### 使用CSS的方法

有三种插入样式表的方法：
+ 外部CSS
+ 内部CSS
+ 行内CSS
  
##### 外部CSS

&emsp;使用外部样式表。

&emsp;外部样式表在HTML页面中head部分，利用`<link>`元素进行引用。

```html
<link rel="stylesheet" type="text/css" href="mystyle.css">
```

##### 内部CSS

&emsp;如果一张 HTML 页面拥有唯一的样式，那么可以使用内部样式表。

&emsp;内部样式是在 head 部分的 `<style>` 元素中进行定义。

##### 行内CSS

&emsp;行内样式（也称内联样式）可用于为单个元素应用唯一的样式。

&emsp;如需使用行内样式，请将 style 属性添加到相关元素。style 属性可包含任何 CSS 属性。

```html
<h1 style="color:blue;text-align:center;">This is a heading</h1>
```

##### 多个样式表

&emsp;如果在不同样式表中为同一选择器（元素）定义了一些属性，则将使用最后读取的样式表中的值。

---

### 层叠顺序

&emsp;当为某个 HTML 元素指定了多个样式时，页面中的所有样式将按照以下规则“层叠”为新的“虚拟”样式表，其中第一优先级最高：

1. 行内样式（在 HTML 元素中）
2. 外部和内部样式表（在 head 部分）
3. 浏览器默认样式

---

<br/>

<h1 id='chapter3'>三、CSS的基础应用</h1>

本章内容：

+ CSS 颜色
+ CSS 背景
+ CSS 边框
+ CSS 轮廓
+ CSS 文本
+ CSS 字体
+ CSS 图标
+ CSS 链接
+ CSS 列表与表格

---



