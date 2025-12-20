//O(n + m), LPS O(m), matching O(n)
#include <iostream>
#include <vector>
using namespace std;

int ans;

vector<int> LPS(const string &pattern)
{
    int n = pattern.size();
    vector<int> lps(n, 0);
    int j = 0;
    int i = 1;
    while (i < n)
    {
        if (pattern[i] == pattern[j])
        {
            lps[i] = j + 1;
            i++;
            j++;
        }
        else
        {
            if (j == 0)
            {
                lps[i] = 0;
                i++;
            }
            else
            {
                j = lps[j - 1];
            }
        }
    }

    return lps;
}

void kmp(const string &text, const string &pattern)
{
    int n = text.size(), m = pattern.size();
    vector<int> lps = LPS(pattern);

    int i = 0, j = 0;

    while (i < n)
    {
        if (text[i] == pattern[j])
        {
            i++;
            j++;
            if (j == m)
            {
                ans++;
                j = lps[j - 1];
            }
        }
        else
        {
            if (j > 0)
            {
                j = lps[j - 1];
            }
            else
            {
                i++;
            }
        }
    }
}

int main(){
    return 0;
}