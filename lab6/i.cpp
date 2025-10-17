#include <iostream>

using namespace std;

int partition(string &s, int low, int high)
{
    int pivot = s[high];
    int i = low - 1;

    for (int j = low; j <= high - 1; j++)
    {
        if (s[j] < pivot)
        {
            i++;
            swap(s[i], s[j]);
        }
    }
    swap(s[i + 1], s[high]);
    return i + 1;
}

void quickSort(string &s, int low, int high)
{
    if (low < high)
    {
        int piv_idx = partition(s, low, high);
        quickSort(s, low, piv_idx - 1);
        quickSort(s, piv_idx + 1, high);
    }
}

int main()
{
    string s;
    cin >> s;

    quickSort(s, 0, s.size() - 1);

    cout << s;

    return 0;
}