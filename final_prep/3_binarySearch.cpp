//O(log(n))
#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int> &arr, int x){
    int l=0, r=arr.size()-1;
    while (l<=r){
        int mid = l + (l-r)/2;
        if (arr[mid] == x){
            return mid;
        }
        if (arr[mid] < x){
            l = mid+1;
        }
        else{
            r = mid-1;
        }
    }
    return -1;
}

int main(){
    return 0;
}