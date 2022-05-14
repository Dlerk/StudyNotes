#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include "Wine.h"

#define maxn 10000+10
#define inf 0x3f3f3f

using std::cout;
using std::cin;
using std::endl;
using std::string;

// constructors
Wine::Wine()
{
    name[0] = '\0';
    storeYears = 0;
}

Wine::Wine(const char * l, int y)
{
    name = l;
    storeYears = y;
}

Wine::Wine(const char * l, int  y, const int yr[], const int bot[])
{
    name = l;
    storeYears = y;
    for( int i=0 ; i<storeYears ; i++ )
    {
        data.a[i] = yr[i];
        data.b[i] = bot[i];
    }
}

// functions
void Wine::GetBottles()
{
    for( int i=0 ; i<storeYears ; i++ )
    {
        cout << "Please input vintage's year and bottles:";
        cin >> data.a[i] >> data.b[i];
        cout << endl;
    }
}

string & Wine::Label() const
{
    return name;
}

int Wine::sum() const
{
    int s = 0;
    for( int i=0 ; i<storeYears ; i++ )
        s += data.b[i];
    
    return s;
}