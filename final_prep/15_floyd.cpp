//O(V^3)
#include <iostream>
#include <vector>
using namespace std;

int main(){
    int v,e;
    cin >> v >> e;
    const int INF = 1e9;
    vector<vector<int> > dist(v, vector<int>(v, INF));
    for (int i=0;i<v;i++){
        dist[i][i]=0;
    }

    for (int i=0;i<e;i++){
        int a,b,weight;
        cin >> a >> b >> weight;
        dist[a][b]=min(dist[a][b], weight);
    }
    for (int vert=0;vert<v;vert++){
        for(int a=0;a<v;a++){
            for (int b=0;b<v;b++){
                if(dist[a][vert] != INF && dist[vert][b] != INF && dist[a][b] > dist[a][vert] + dist[vert][b]){
                    dist[a][b] = dist[a][vert] + dist[vert][b];
                }
            }
        }
    }
    return 0;
}