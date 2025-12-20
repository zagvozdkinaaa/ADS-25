//O(V+E)
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void dfs(vector<vector<int> > &graph, vector<int> &visited, int vert, vector<int> &order){
    visited[vert] = 1;
    
    for (int to : graph[vert]){
        if (!visited[to]){
            dfs(graph, visited, to, order);
        }
    }
    order.push_back(vert);
}

int main(){
    int v, e;
    cin >> v >> e;
    vector<vector<int> > graph(v);
    for (int i=0; i<e; i++){
        int a,b;
        cin >> a >> b;

        graph[a].push_back(b);
    }
    vector<int> visited(v, 0);
    vector<int> order;

    for (int i=0; i<v; i++){
        if (!visited[i]){
            dfs(graph, visited, i, order);
        }
    }
    reverse(order.begin(), order.end());

    for (int v : order){
        cout << v;
    }
    
    return 0;
}