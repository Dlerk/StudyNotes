#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include "CD.h"

#define maxn 10000+10
#define inf 0x3f3f3f

using std::cout;
using std::cin;
using std::endl;
using std::string;

// CD

CD::CD()
{
    performers[0] = '\0';
    label[0] = '\0';
    selections = 0;
    playtime = 0;
}

CD::CD(const CD & d)
{
    strcpy(performers, d.performers);
    strcpy(label, d.label);
    selections = d.selections;
    playtime = d.playtime;
}

CD::CD(const char * s1, const char * s2, int n, double x)
{
    strcpy(performers, s1);
    strcpy(label, s2);
    selections = n;
    playtime = x;
}

CD & CD::operator=(const CD & d)
{
    strcpy(performers, d.performers);
    strcpy(label, d.label);
    selections = d.selections;
    playtime = d.playtime;
    return *this;
}

void CD::report() const
{
    cout << endl;
    cout << performers << endl;
    cout << label << endl;
    cout << selections << endl;
    cout << playtime << endl;
}

// Classic

Classic::Classic()
{
    name[0] = '\0';
}

Classic::Classic(const char * s1, const char * s2, int n, double x, const char * na)
        : CD(s1, s2, n, x)
{
    strcpy(name, na);
}

Classic::Classic(const Classic & c)
        : CD(c)
{
    strcpy(name, c.name);
}

void Classic::report() const
{

    cout << endl;
    cout << name << endl;
    CD::report();

} 