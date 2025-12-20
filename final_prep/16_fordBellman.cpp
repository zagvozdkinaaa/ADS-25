//O(VE)
#include <iostream>
#include <vector>
using namespace std;

const int INF = 1e9;

struct Edge{
    int a, b, weight;
};

vector<int> fordBellman(vector<Edge> &edges, int v, int start){
    vector<int> dist(v, INF);
    dist[start] = 0;
    for (int i=0;i<v-1;i++){
        for(auto &[a,b,weight] : edges){
            if(dist[a] != INF && dist[b] > dist[a] + weight){
                dist[b] = dist[a] + weight;
            }
        }
    }
    return dist;
}

int main(){
    int v, e;
    cin >> v >> e;
    vector<Edge> edges(e);
    for (auto &[a,b,weight] : edges){
        cin >> a >> b >> weight;
    }
    return 0;
}