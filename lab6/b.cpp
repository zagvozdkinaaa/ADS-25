#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<int> a(n), b(m);

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++)
    {
        cin >> b[i];
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    vector<int> common;
    set_intersection(a.begin(), a.end(), b.begin(), b.end(), back_inserter(common));

    for (int i = 0; i < common.size(); i++)
        cout << common[i] << " ";

    return 0;
}