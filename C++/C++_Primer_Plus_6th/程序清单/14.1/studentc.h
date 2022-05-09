#ifndef _STUDENTC_H_
#define _STUDENTC_H_

#include <iostream>
#include <string>
#include <valarray>

class Student
{

private:
    typedef std::valarray<double> ArrayDb;
    std::string name;
    ArrayDb scores;
    std::ostream & arr_out(std::ostream & os) const; 

public:
    Student() : name("Null Student"), scores() {}
    explicit Student(const std::string & s)
        : name(s), scores() {}
    explicit Student(int n) : name("Nully"), scores() {}
    /*
        使用explicit关闭单参数构造函数的隐式转换
        防止出现将某Student对象，例如Student dop("Homer",10)
        赋值时将dop[0]=5，写成dop=5
        使得编译器调用该构造函数Student(5)创建临时Student对象
        并将该临时Student对象的值赋值给dop对象
    */ 
    Student(const std::string & s, int n)
        : name(s), scores(n) {}
    Student(const char * str, const double * pd, int n)
        : name(str), scores(pd, n) {}
    ~Student() {}    

    double Average() const;
    const std::string & Name() const;
    double & operator[](int i);
    double operator[](int i) const; 

// friends
    //input
    friend std::istream & operator>>(std::istream & is, Student & stu);
    friend std::istream & getline(std::istream & is, Student & stu);
    //output
    friend std::ostream & operator<<(std::ostream & os, const Student & stu);

}


#endif