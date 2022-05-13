#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include "Port.h"

#define maxn 10000+10
#define inf 0x3f3f3f

using std::cout;
using std::cin;
using std::endl;
using std::string;

// Port

Port::Port(const Port & p)
{
    brand = new char[ strlen(p.brand)+1 ];

    strcpy(brand, p.brand);
    strcpy(style, p.style);
    bottles = p.bottles;
}

Port::Port(const char * br="None", const char * st="None", int b=0)
{
    brand = new char[ strlen(br)+1 ];

    strcpy(brand, br);
    strcpy(style, st);
    bottles = b;
}

// VintagePort

VintagePort::VintagePort()
            : Port()
{
    nickname = new char[1];
    nickname[0] = '\0';
    year = 0;
}

VintagePort::VintagePort(const VintagePort & vp)
            : Port(vp)
{
    nickname = new char[ strlen(vp.nickname)+1 ];
    strcpy(nickname, vp.nickname);
}

VintagePort::VintagePort(const char * br, const char * st, int b, const char * nn, int y)
            : Port(br, st, b)
{
    nickname = new char[ strlen(nn)+1 ];
    strcpy(nickname, nn);
}



VintagePort & VintagePort::operator=(const VintagePort & vp)
{
    delete [] nickname;

    nickname = new char[ strlen(vp.nickname)+1 ];
    strcpy(nickname, vp.nickname);
}

ostream & operator<<(ostream & os, const VintagePort & vp)
{
    os << vp.nickname << vp.BottleCount() << vp.year;
    return os;
}



void  VintagePort::Show() const
{
    Port::Show();
    cout << *this;
}
