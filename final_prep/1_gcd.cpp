//O(log(min(a, b)))
#include <iostream>
using namespace std;

int gcd(int a, int b){
    while(b!=0){
        int r = a%b;
        a=b;
        b=r;
    }
    return a;
}

int main(){
    return 0;
}