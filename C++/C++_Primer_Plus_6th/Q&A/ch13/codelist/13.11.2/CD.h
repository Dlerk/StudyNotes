#ifndef _CD_H_
#define _CD_H_

class CD
{

private:

    char * performers;
    char * label;
    int selections;
    double playtime;
    
public:

// constructors
    CD();
    CD(const CD & d);
    CD(const char * s1, const char * s2, int n, double x);
    ~CD() { delete[] performers; delete[] label; }

// other functions
    CD & operator=(const CD & d);
    virtual void report() const;

};

class Classic: public CD
{

private:

    char * name;

public:

// constructors
    Classic();
    Classic(const char * s1, const char * s2, int n, double x, const char * na);
    Classic(const Classic & c);
    ~Classic() { delete[] name; }

// other functions
    void report() const;

};

#endif