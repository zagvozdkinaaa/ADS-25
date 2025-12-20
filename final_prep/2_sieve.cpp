//O(n*log(log(n)))
#include <iostream>
#include <vector>
using namespace std;
vector<int> sieve(int n){
    vector<bool> prime(n+1, true);
    for(int p=2; p*p<=n; p++){
        if(prime[p]==true){
            for(int i=p*p; i<=n; i+=p){
                prime[p]=false;
            }
        }
    }
    vector<int> res;
    for(int p=2; p<=n; p++){
        if(prime[p]){
            res.push_back(p);
        }
    }
    return res;
}

int main(){
    return 0;
}