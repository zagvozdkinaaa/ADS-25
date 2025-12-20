// O(V^2+E) for dense, O((V+E)log(V)) for sparse
#include <iostream>
#include <vector>
#include <set>
using namespace std;

const int INF = 1e9;

vector<int> dijkstra(vector<vector<pair<int, int> > > &graph, int start){
    vector<int> dist(graph.size(), INF);
    dist[start]=0;
    set<pair<int, int> > q;
    q.insert({dist[start], start});

    while(!q.empty()){
        int nearest = q.begin()->second;
        q.erase(q.begin());
        for(auto &[to, weight] : graph[nearest]){
            if(dist[to] > dist[nearest] + weight){
                q.erase({dist[to], to});
                dist[to] = dist[nearest] + weight;
                q.insert({dist[to], to});
            }
        }
    }
    return dist;
}

int main(){
    int v, e;
    cin >> v >> e;
    vector<vector<pair<int, int> > > graph(v);
    for (int i=0; i<e; i++){
        int a,b,weight;
        cin >> a >> b >> weight;

        graph[a].push_back({b,weight});
    }

    
    return 0;
}