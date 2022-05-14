#ifndef _WINE_H_
#define _WINE_H_
#include <string>
#include <valarray>

using std::string;
using std::valarray;

template <class T1, class T2>
class Pair
{
private:
    
    T1 a;
    T2 b;

public:

    T1 & first() { return a; }
    T1 first() const { return a; }
    T2 & second() { return b; }
    T2 second() const { return b; }
    Pair() {};
    Pair(const T1 & aval, const T2 & bval) : a(aval), b(bval) {}

};

// Pari x;  x.first(); 
/*
 调用前一个版本，返回指向 a 成员的引用           
 可通过 x.first() 修改 x 对象的 a 成员 
*/

//const Pari cx; cx.first(); 
/* 
 调用后一个版本，返回 a 成员的一个副本            
 不可通过 x.first() 修改 cx 对象的 a 成员
*/

// 非 const 版本返回可修改的引用，const 版本返回不可修改的值

typedef std::valarray<int> ArrayInt;
typedef Pair<ArrayInt, ArrayInt> PairArray;

class Wine
{

private:
    
    string name;
    PairArray data;
    // Pair.a = years, Pair.b = numbers
    int storeYears;

public:

// constructors
    Wine();
    Wine(const char * l, int y);
    Wine(const char * l, int  y, const int yr[], const int bot[]);
    ~Wine() {}

// functions
    void GetBottles() ;
    string & Label() const;
    int sum() const;

};


#endif