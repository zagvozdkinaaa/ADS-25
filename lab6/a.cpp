#include <iostream>
#include <algorithm>
using namespace std;

bool isVowel(char c)
{
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

bool compare(char a, char b)
{
    bool va = isVowel(a);
    bool vb = isVowel(b);

    if (va != vb)
        return va;
    return a < b;
}

int main()
{
    int n;
    string s;
    cin >> n >> s;

    sort(s.begin(), s.end(), compare);

    cout << s;
    return 0;
}