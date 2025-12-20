//O(n + m)
#include <iostream>
#include <vector>
using namespace std;

const int p = 31; 
const int m = 1e9 + 9;

long long compute_hash(const string &s) {
    long long hash = 0, p_pow = 1;
    for(char c : s) {
        hash = (hash + (c-'a'+1)*p_pow) % m;
        p_pow = (p_pow * p) % m;
    }
    return hash;
}

void rabinKarp(const string &text, const string &pattern) {
    int n = text.size(), m_ = pattern.size();
    long long p_hash = compute_hash(pattern);
    long long t_hash = compute_hash(text.substr(0, m_));
    long long p_pow = 1;
    for(int i=0;i<m_;i++) p_pow = (p_pow*p)%m;

    for(int i=0;i+n<=n;i++) {
        if(t_hash==p_hash && text.substr(i,m_)==pattern) 
            cout<<"Pattern at index "<<i<<"\n";
        if(i+n<m) 
            t_hash = ((t_hash-(text[i]-'a'+1)+::m)/p + (text[i+m_]-'a'+1)*p_pow)%m;
    }
}

int main(){
    return 0;
}