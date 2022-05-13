/**
 * @a 见Port.cpp
 * @b 派生类会自动调用基类的方法。因此仅有需要使用动态内存分配的方法，需要重新定义
 * @c 重载赋值运算符函数虽然可以被声明为虚函数，但是没有意义。重载<<运算符为Port类的友元函数,不是类成员
 * @d 见Port.cpp
 */

#ifndef _PORT_H_
#define _PORT_H_

#include <iostream>
using std::ostream;

class Port
{

private:

    char * brand;
    char style[20];
    int bottles;

public:

// ocnstructors
    Port(const Port & p);
    Port(const char * br="None", const char * st="None", int b=0);
    virtual ~Port();

// reloaded operators
    Port & operator=(const Port & p);
    Port & operator+=(int b);
    Port & operator-=(int b);

// functions
    int BottleCount() const { return bottles; } 
    virtual void Show() const;
    friend ostream & operator<<(ostream & os, const Port & p);

};

class VintagePort : public Port
{

private:
    
    char * nickname;
    int year;

public:

// constructors
    VintagePort();
    VintagePort(const VintagePort & vp);
    VintagePort(const char * br, const char * st, int b, const char * nn, int y);
    ~ VintagePort() { delete[] nickname; }

// operators
    VintagePort & operator=(const VintagePort & vp);
    friend ostream & operator<<(ostream & os, const VintagePort & vp);

// functions
    void Show() const;

};




#endif