#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

struct Student
{
    string name;
    string surname;
    double gpa;
};

bool cmp(Student a, Student b)
{
    if (a.gpa != b.gpa)
        return a.gpa < b.gpa;
    if (a.surname != b.surname)
        return a.surname < b.surname;
    return a.name < b.name;
}

int partition(vector<Student> &arr, int low, int high)
{
    Student pivot = arr[high];
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

void quickSort(vector<Student> &arr, int low, int high)
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
    string mark;
    double credits;

    cin >> n;

    vector<Student> s(n);
    for (int i = 0; i < n; i++)
    {
        cin >> s[i].surname >> s[i].name >> m;
        double sum_of_credits = 0;
        double sum_of_gpa = 0;
        for (int j = 0; j < m; j++)
        {
            cin >> mark >> credits;
            if (mark == "A+")
                sum_of_gpa += (4.0 * credits);
            if (mark == "A")
                sum_of_gpa += (3.75 * credits);
            if (mark == "B+")
                sum_of_gpa += (3.5 * credits);
            if (mark == "B")
                sum_of_gpa += (3.0 * credits);
            if (mark == "C+")
                sum_of_gpa += (2.5 * credits);
            if (mark == "C")
                sum_of_gpa += (2.0 * credits);
            if (mark == "D+")
                sum_of_gpa += (1.5 * credits);
            if (mark == "D")
                sum_of_gpa += (1.0 * credits);
            if (mark == "F")
                sum_of_gpa += (0 * credits);
            sum_of_credits += credits;
        }
        s[i].gpa = sum_of_gpa / double(sum_of_credits);
    }

    quickSort(s, 0, n - 1);

    for (int i = 0; i < n; i++)
    {
        cout << s[i].surname << ' ' << s[i].name << ' ' << fixed << setprecision(3) << s[i].gpa << '\n';
    }

    return 0;
}