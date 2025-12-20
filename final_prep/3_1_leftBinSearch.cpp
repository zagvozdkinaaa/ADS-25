//O(log(n))
#include <iostream>
#include <vector>
using namespace std;

int leftBinarySearch(vector<int> &arr, int x){
    int l=0, r=arr.size()-1;
    while (l+1<r){
        int mid = l + (l-r)/2;
        
        if (arr[mid] < x){
            l = mid;
        }
        else{
            r = mid;
        }
    }
    if(arr[l] == x){
        return l;
    }
    if(arr[r] == x){
        return r;
    }
    return -1;
}

int main(){
    return 0;
}