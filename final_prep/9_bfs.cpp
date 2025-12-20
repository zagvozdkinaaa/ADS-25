//O(V+E)
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector <int> bfs(vector <vector <int> > &graph){
    int n = graph.size();
    vector <bool> visited(n, false);
    vector <int> res;
    queue <int> q;

    q.push(0);
    visited[0]=true;

    while (!q.empty()){
        int cur = q.front();
        q.pop();
        res.push_back(cur);
        for(int x : graph[cur]){
            if (!visited[x]){
                visited[x]=true;
                q.push(x);
            }
        }
    }
    return res;
}

int main(){
    return 0;
}