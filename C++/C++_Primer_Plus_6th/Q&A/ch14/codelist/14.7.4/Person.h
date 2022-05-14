#ifndef _PERSON_H_
#define _PERSON_H_
#include "Poker.hpp"

class Person
{

private:
    
    char * name;

public:

// cosntructors
    Person();
    Person(const char * n);
    ~Person() { delete[] name; }

// functions    

    virtual void Show() const;
    

};

class Gunslinger
{
private:

    int scars;

public:

    Gunslinger(const char * n, int s);
    ~Gunslinger() {}

    void Show() const;
    double draw();

};

class PokerPlayer : virtual public Person
{

public:

    PokerPlayer(const char * n) : Person(n) {}
    ~PokerPlayer() {}

    Card Draw() const;

};

class BadDude : Gunslinger, PokerPlayer
{

public:

    BadDude();
    ~BadDude();

    void Gdraw() const;
    void Cdraw() const;
    void Show() const;

};

#endif