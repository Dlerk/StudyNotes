#ifndef STOCK_H_
#define STOCK_H_

#include <iostream>

using std::ostream;
using std::istream;

class Stock
{

private:

    char * str;
    int shares;
    double share_val;
    double total_val;
    void set_tot() { total_val= shares*share_val; }

public:

// constructors
    Stock();
    Stock(const char * s, long n, double pr);
    ~Stock() { delete [] str; }

//friends
    friend ostream & operator<<(ostream & os, const Stock & st);

};





#endif STOCK_H_