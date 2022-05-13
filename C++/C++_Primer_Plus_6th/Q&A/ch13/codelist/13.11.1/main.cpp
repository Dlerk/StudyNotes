#include <stdio.h>
#include <iostream>
#include "CD.h"

#define maxn 10000+10
#define inf 0x3f3f3f

using namespace std ;



int main()
{

    CD blank;
    CD Animation("希望の花", "二刺猿", 1, 335);

    Classic A("a-per", "a-tag", 114, 514, "A-NAME");

    blank.report();
    cout << endl;
    Animation.report();
    
    blank = Animation;
    blank.report();
    cout << endl;

    A.report();

    return 0 ;
}