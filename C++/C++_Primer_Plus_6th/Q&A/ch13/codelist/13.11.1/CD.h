#ifndef _CD_H_
#define _CD_H_

class CD
{

private:

    char performers[50];
    char label[20];
    int selections;
    double playtime;
    
public:

// constructors
    CD();
    CD(const CD & d);
    CD(const char * s1, const char * s2, int n, double x);
    ~CD() {};

// other functions
    CD & operator=(const CD & d);
    virtual void report() const;

};

class Classic: public CD
{

private:

    char name[50];

public:

// constructors
    Classic();
    Classic(const char * s1, const char * s2, int n, double x, const char * na);
    Classic(const Classic & c);
    ~Classic() {};

// other functions
    void report() const;

};

#endif