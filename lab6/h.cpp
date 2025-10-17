#include <iostream>

using namespace std;

int partition(char *arr, int low, int high)
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

void quickSort(char *arr, int low, int high)
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
    char a;
    cin >> n;
    char letters[n];

    for (int i = 0; i < n; i++)
    {
        cin >> letters[i];
    }

    cin >> a;

    quickSort(letters, 0, n - 1);

    for (int i = 0; i < n; i++)
    {
        if (letters[i] > a)
        {
            cout << letters[i];
            return 0;
        }
    }

    cout << letters[0];

    return 0;
}