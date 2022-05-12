#include <stdio.h>
#include <iostream>
#include "Cow.h"

#define maxn 10000+10
#define inf 0x3f3f3f

using namespace std ;



int main()
{

    Cow Alice;
    Cow Bob( "Bob", "dance", 10 );
    Cow Jack(Alice);

    Alice.ShowCow();
    Bob.ShowCow();
    Jack.ShowCow();

    Jack = Bob;
    cout << "-------------\n";

    Alice.ShowCow();
    Bob.ShowCow();
    Jack.ShowCow();
    
    cout << endl;

    return 0 ;
}