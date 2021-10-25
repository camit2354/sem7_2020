#include <iostream>
#include <vector>
using namespace std;

void display_graph(const vector<vector<int>> &graph)
{
    int n = graph.size();
    cout << "\n\n graph :\n";
    for (int i = 0; i < n; i++)
    {

        for (int j = 0; j < n; j++)
        {
            cout << graph[i][j] << ' ';
        }
        cout << '\n';
    }

    cout << "\n\n";
}

int main()
{
    int n;
    cout << "\nenter no of nodes -> : \t";
    cin >> n;

    int wt_limit = n * 10;
    vector<vector<int>> graph(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++)
    {
        int randval = 1 + (rand() % wt_limit);
        graph[i][(i + 1) % n] = randval;
        graph[(i + 1) % n][i] = randval;
    }

    display_graph(graph);
    int density = 3;
    int threshold = wt_limit / density;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            int prob = rand() % wt_limit;
            if (graph[i][j] == 0 && prob <= threshold)
            {
                int randwt = rand() % wt_limit + 1;
                graph[i][j] = randwt;
                graph[j][i] = randwt;
            }
        }
    }

    display_graph(graph);
    return 0;
}