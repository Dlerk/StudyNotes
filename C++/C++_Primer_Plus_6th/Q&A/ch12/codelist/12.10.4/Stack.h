#ifndef _STACK_H_
#define _STACK_H_

class Stack
{
 private:

    int * pitems;
    int size;
    int top;

 public:

    Stack(int n = 10);
    Stack(const Stack & st);
    ~Stack();

};

#endif