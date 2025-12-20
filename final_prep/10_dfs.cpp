//O(V+E)
#include <iostream>
#include <vector>
using namespace std;

void dfs(vector<vector<int> > &graph, vector<int> &visited, int vert){
    visited[vert] = 1;
    
    for (int to : graph[vert]){
        if (!visited[to]){
            dfs(graph, visited, to);
        }
    }
}

int main(){
    int v, e;
    cin >> v >> e;
    vector<vector<int> > graph(v);
    for (int i=0; i<e; i++){
        int a,b;
        cin >> a >> b;

        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    vector<int> visited(v, 0);
    
    return 0;
}