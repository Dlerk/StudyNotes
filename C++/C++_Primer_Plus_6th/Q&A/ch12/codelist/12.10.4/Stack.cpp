#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include "Stack.h"

#define maxn 10000+10
#define inf 0x3f3f3f

using std::cout;
using std::cin;
using std::endl;
using std::string;


Stack::Stack(int n = 10)
{
    top = n;
    pitems = new int[n];
    for( int i=0 ; i<n ; i++ )
        cin >> pitems[i];
}


Stack::Stack(const Stack & st)
{
    top = st.top;
    pitems = new int[top];
    for( int i=0 ; i<top ; i++ )
        cin >> pitems[i];
}



Stack::~Stack()
{
    delete [] pitems;
}
