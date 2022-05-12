#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include "Cow.h"

using std::cout;
using std::cin;
using std::endl;
using std::string;

Cow::Cow()
{
    name[0] = '\0';
    hobby = new char[1];
    hobby[0] = '\0';
    weight = 0;
}

Cow::Cow(const char * nm, const char * ho, double wt)
{
    strcpy(name, nm);
    hobby = new char[strlen(nm)+1];
    strcpy(hobby, ho);
    weight = wt;
}

Cow::Cow(const Cow & c)
{
    strcpy(name, c.name);
    hobby = new char[strlen(c.hobby)+1];
    strcpy(this->hobby, c.hobby);
    weight = c.weight;
}

Cow::~Cow()
{
    cout << name << "is deleted." << endl;
    delete [] hobby;
}

Cow & Cow::operator=(const Cow & c)
{
    strcpy(this->name, c.name);
    delete [] hobby;
    hobby = new char[strlen(c.hobby)+1];
    strcpy(this->hobby, c.hobby);
    weight = c.weight;
    return *this;
}

void Cow::ShowCow() const
{
    cout << endl;
    cout << "Name:" << name << endl;
    cout << "Hobby:" << hobby << endl;
    cout << "Weight:" << weight << endl;
}




