#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n;
    string old, neww;
    map<string, string> mp;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> old >> neww;
        bool found = false;
        for (auto it : mp)
        {
            if (it.second == old)
            {
                mp[it.first] = neww;
                found = true;
            }
        }
        if (!found)
            mp[old] = neww;
    }

    cout << mp.size() << '\n';
    for (auto it : mp)
        cout << it.first << ' ' << it.second << '\n';

    return 0;
}