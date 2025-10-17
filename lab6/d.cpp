#include <iostream>
#include <vector>
using namespace std;

struct Date
{
    int day;
    int month;
    int year;
};

bool cmp(Date &a, Date &b)
{
    if (a.year != b.year)
        return a.year < b.year;
    if (a.month != b.month)
        return a.month < b.month;
    return a.day < b.day;
}

int partition(vector<Date> &arr, int low, int high)
{
    Date pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++)
    {
        if (cmp(arr[j], pivot))
        {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<Date> &arr, int low, int high)
{
    if (low < high)
    {
        int piv_idx = partition(arr, low, high);
        quickSort(arr, low, piv_idx - 1);
        quickSort(arr, piv_idx + 1, high);
    }
}

int main()
{
    int n;
    cin >> n;
    string s;
    vector<Date> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> s;
        arr[i].day = (s[0] - '0') * 10 + (s[1] - '0');
        arr[i].month = (s[3] - '0') * 10 + (s[4] - '0');
        arr[i].year = (s[6] - '0') * 1000 + (s[7] - '0') * 100 + (s[8] - '0') * 10 + (s[9] - '0');
    }

    quickSort(arr, 0, n - 1);

    for (int i = 0; i < n; i++)
    {
        if (arr[i].day < 10)
            cout << 0 << arr[i].day << '-';
        else
            cout << arr[i].day << '-';
        if (arr[i].month < 10)
            cout << 0 << arr[i].month << '-';
        else
            cout << arr[i].month << '-';
        cout << arr[i].year << '\n';
    }
    return 0;
}