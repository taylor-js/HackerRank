#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <string>
using namespace std;

template <class T> class AddElements {
    public:
        T element;
        AddElements(T i) {element = i;}
        T add(T i) {return element+i;}
    private:
        
};
template <> class AddElements <string> {
    public:
        string str_ele;
        AddElements(string i) {str_ele = i;}
        string concatenate(string ele) {return str_ele+ele;}
    private:
        
};