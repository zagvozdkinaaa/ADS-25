#include <iostream>
#include <algorithm>
using namespace std;

int partition(int *arr, int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j <= high - 1; j++)
    {
        if (arr[j] > pivot)
        {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(int *arr, int low, int high)
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
    int n, m;
    cin >> n >> m;
    int arr[n][m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
        }
    }

    for (int j = 0; j < m; j++)
    {
        int columns[n];
        for (int i = 0; i < n; i++)
        {
            columns[i] = arr[i][j];
        }
        quickSort(columns, 0, n - 1);

        for (int i = 0; i < n; i++)
        {
            arr[i][j] = columns[i];
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << arr[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}