#ifndef _STRING2_H_
#define _STRING2_H_

#include <iostream>

using std::ostream;
using std::istream;


class String
{

private:

    char * str;
    int len;
    static int num_strings;
    static const int CINLIM = 80;

public:

// constructors and other methods
    String();
    String(const char * s);
    String(const String &);
    ~String();
    int length () const { return len; }

// overloaded operator methods
    String & operator=(const String &);
    String & operator=(const char *);
    char & operator[](int i);
    const char & operator[](int i) const;

// overloaded operator friends
    friend bool operator<(const String &st, const String &st2);
    friend bool operator>(const String &st, const String &st2);
    friend bool operator==(const String &st, const String &st2);
    friend ostream & operator<<(ostream & os, const String & st); 
    friend istream & operator>>(ostream & is, const String & st); 

//static function
    static int HowMant();

// new add
    friend String operator+(const String &st, const String &st2);
    void Stringlow();
    void Stringup();
    int occurs(char tar);

};

#endif