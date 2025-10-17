#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &arr, int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j <= high - 1; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<int> &arr, int low, int high)
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
    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    quickSort(arr, 0, n - 1);
    int min_diff = 1000000;
    for (int i = 0; i < n - 1; i++)
    {
        int diff = arr[i + 1] - arr[i];
        if (diff < min_diff)
        {
            min_diff = diff;
        }
    }

    for (int i = 0; i < n - 1; i++)
    {
        if (arr[i + 1] - arr[i] == min_diff)
        {
            cout << arr[i] << ' ' << arr[i + 1] << ' ';
        }
    }

    return 0;
}