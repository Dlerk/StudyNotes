#ifndef _Poker_H_
#define _Poker_H_

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>

#define maxn 10000+10
#define inf 0x3f3f3f

using std::cout;
using std::cin;
using std::endl;
using std::string;

class Poker
{

private:
    
    int num;
    char suit;

public:

    Poker() {}
    Poker(int n, char s);
    ~Poker() {}

    void show() const;

};

/*
    cout << "Choose a suit:" << endl;
    cout << "S for ♠\n";
    cout << "H for ♥\n";
    cout << "C for ♣\n";
    cout << "D for ♦\n";
*/

Poker::Poker(int n, char s)
{
    while( n>13 || n<1 )
    {
        cout << "You input a wrong number!"
             << "Please input a number between 1~13.\n";
        cin >> n;
    }

    num = n ;
    switch (s)
    {
    case 'S':
        suit = '♠';
        break;

    case 'H':
        suit = '♥';
        break;

    case 'C':
        suit = '♣';
        break;

    case 'D':
        suit = '♦';
        break;
    }    
}

void Poker::show() const
{

    cout << "----------\n";
    cout << suit << "   ";

    if( num == 1 )
        cout << 'A' << endl;
    else if( num>10 )
    {
        switch (num)
        {
        case 11:
            cout << 'J' << endl;
            break;
        
        case 12:
            cout << 'Q' << endl;
            break;
        
        case 13:
            cout << 'K' << endl;
            break;
        }
    }

    cout << "----------\n";
}

#endif 