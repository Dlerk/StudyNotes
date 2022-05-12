#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include "Stock.h"

#define maxn 10000+10
#define inf 0x3f3f3f

using std::cout;
using std::cin;
using std::endl;
using std::string;

Stock::Stock()
{
    str = new char[1];
    str[0] = '\0';
}

Stock::Stock(const char * s, long n, double pr)
{
    int len = strlen(s);
    str = new char[len+1];
    strcpy(str, s);
    //···
}

ostream & operator<<(ostream & os, const Stock & st)
{
    os << st.str << st.shares << st.total_val;
    return os;
}