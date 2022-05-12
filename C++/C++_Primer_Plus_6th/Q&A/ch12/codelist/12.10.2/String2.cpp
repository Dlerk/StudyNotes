#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <ctype.h>
#include "String2.h"

#define maxn 10000+10
#define inf 0x3f3f3f

using std::cout;
using std::cin;
using std::endl;
using std::string;

String operator+(const String &st, const String &st2)
{
    String sum;

    sum.len = st.len + st2.len;
    sum.str = new char[sum.len+1];
    strcpy(sum.str, st.str);
    strcat(sum.str, st2.str);

    return sum;
}

void String::Stringlow()
{
    for( int i=0 ; i<len ; i++ )  
    {
        if( isupper(str[i]) )
            tolower(str[i]);
    }
}

void String::Stringup()
{
    for( int i=0 ; i<len ; i++ )  
    {
        if( islower(str[i]) )
            toupper(str[i]);
    }
}

int String::occurs(char tar)
{
    int cnt=0;
    for( int i=0 ; i<len ; i++ )  
    {
        if( str[i] == tar )
            ++cnt;
    }

    return cnt;
}
