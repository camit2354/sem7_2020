#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

#define INF 10000

int populationLimit = 50;
vector<vector<int>> graph;
int fitness_value(const vector<int> &person);

bool comp(const vector<int> &a, const vector<int> &b);
vector<pair<int, int>> *gen_input_graph_random(int n);
vector<pair<int, int>> *user_input(int n);
vector<vector<int>> generate_population(int n);
vector<vector<int>> adjTograph(vector<pair<int, int>> *adj, int n);

void display_graph(const vector<vector<int>> &graph);
void display_adj(vector<pair<int, int>> *adj, int n);
void display_population(const vector<vector<int>> &graph, const vector<vector<int>> &population);

vector<vector<int>> cross_over(const vector<vector<int>> &population);
vector<vector<int>> mutation(vector<vector<int>> population);
vector<vector<int>> survival_of_fittest(const vector<vector<int>> &population, const vector<vector<int>> &newpopulation);

int main()
{
    int n;
    cout << "Enter no of nodes for graph creation \n";
    cin >> n;

    int choice;
    cout << "\n1.do u want random generated graph 2. user input graph -> \t ";
    cin >> choice;

    vector<pair<int, int>> *adj;

    if (choice == 1)
    {
        adj = gen_input_graph_random(n);
    }
    else if (choice == 2)
    {

        adj = user_input(n);
    }
    else
    {
        cout << "invalid choice \n";
        exit(0);
    }

    // display_adj(adj, n);
    graph = adjTograph(adj, n);
    display_graph(graph);

    vector<vector<int>> population = generate_population(n);
    display_population(graph, population);

    vector<vector<int>> cross_over_population, mutation_population, newpopulation;
    cout << "\n Enter no of generations u want to consider -> \t";
    int genCnt;
    cin >> genCnt;

    for (int i = 0; i < genCnt; i++)
    {

        cross_over_population = cross_over(population);
        // display_population(graph, cross_over_population);

        mutation_population = mutation(population);
        // display_population(graph, mutation_population);

        newpopulation = survival_of_fittest(population, mutation_population);
        // display_population(graph, newpopulation);

        population = newpopulation;
        display_population(graph, population);
    }

    return 0;
}

bool comp(const vector<int> &a, const vector<int> &b)
{
    return (fitness_value(a) < fitness_value(b));
}

vector<vector<int>> survival_of_fittest(const vector<vector<int>> &population, const vector<vector<int>> &newpopulation)
{
    vector<vector<int>> total_population;
    int n = population.size();

    for (int i = 0; i < n; i++)
    {
        total_population.push_back(population[i]);
        total_population.push_back(newpopulation[i]);
    }

    sort(total_population.begin(), total_population.end(), &comp);

    vector<vector<int>> ret;
    for (int i = 0; i < populationLimit && i < 2 * n; i++)
    {
        ret.push_back(total_population[i]);
    }
    return ret;
}

vector<vector<int>> cross_over(const vector<vector<int>> &population)
{
    vector<vector<int>> newpopulation;
    int n = population.size(), m = population[0].size();
    int crosspoint = m * (0.75);
    // cout << "\n cross over point " << crosspoint;

    for (int i = 0; i < n / 2; i++)
    {
        int x, y;
        x = rand() % m;
        y = rand() % m;
        while (x == y)
        {
            y = rand() % m;
        }

        // cout << "\n selected male , female" << x << ' ' << y;

        vector<int> male = population[x];
        vector<int> female = population[y];

        vector<int> child1 = male, child2 = female;
        for (int j = crosspoint; j < m; j++)
        {
            int idx1 = j, idx2 = j;
            child1[j] = female[j];
            for (int k = 0; k < m; k++)
            {
                if (female[j] == male[k])
                {
                    idx1 = k;
                    break;
                }
            }
            child1[idx1] = male[j];

            child2[j] = male[j];
            for (int k = 0; k < m; k++)
            {
                if (male[j] == female[k])
                {
                    idx2 = k;
                    break;
                }
            }

            child2[idx2] = female[j];
        }

        newpopulation.push_back(child1);
        newpopulation.push_back(child2);
    }

    return newpopulation;
}

vector<vector<int>> mutation(vector<vector<int>> population)
{
    float mutation_percent = 0.1;
    int n = population.size(), m = population[0].size();
    float threshold = mutation_percent * float(m);
    // cout << "\n threshold : " << threshold << '\n';
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < int(threshold); j++)
        {
            int x = rand() % m;
            int value = rand() % m + 1;
            int y = -1;
            for (int k = 0; k < m; k++)
            {
                if (value == population[i][k])
                {
                    y = k;
                    break;
                }
            }

            int temp = population[i][x];
            population[i][x] = population[i][y];
            population[i][y] = temp;
        }
    }

    return population;
}

void display_adj(vector<pair<int, int>> *adj, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << "i : \t" << i << '\t';
        for (auto &p : adj[i])
        {
            cout << "( " << p.first << " , " << p.second << " ) \t";
        }
        cout << '\n';
    }
}

void display_graph(const vector<vector<int>> &graph)
{
    cout << " \n graph matrix : ";
    int n = graph.size();
    for (int i = 0; i < n; i++)
    {
        cout << '\n';
        for (int j = 0; j < n; j++)
        {
            cout << graph[i][j] << ' ';
        }
    }

    cout << '\n';

    return;
}

vector<vector<int>> adjTograph(vector<pair<int, int>> *adj, int n)
{
    vector<vector<int>> graph(n, vector<int>(n, INF));
    for (int i = 0; i < n; i++)
    {
        for (auto &p : adj[i])
        {
            graph[i][p.first] = p.second;
            graph[p.first][i] = p.second;
        }
    }

    return graph;
}

vector<pair<int, int>> *user_input(int n)
{

    int choice;
    cout << "\n 1.user matrix input 2 . user edges input -> \t";
    cin >> choice;

    vector<vector<int>> graph(n, vector<int>(n, 0));

    if (choice == 1)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cin >> graph[i][j];
            }
        }
    }
    else if (choice == 2)
    {
        int n;
        cout << "\nenter no of edges -> \t";
        cin >> n;

        while (n--)
        {
            int i, j, wt;
            cin >> i >> j >> wt;
            graph[i][j] = wt;
            graph[j][i] = wt;
        }
    }
    else
    {
        cout << "\n invalid choice \n";
        exit(0);
    }

    vector<pair<int, int>> *adj = new vector<pair<int, int>>[n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (graph[i][j] != 0)
            {
                adj[i].push_back({j, graph[i][j]});
                adj[j].push_back({i, graph[i][j]});
            }
        }
    }

    return adj;
}

vector<pair<int, int>> *gen_input_graph_random(int n)
{
    int weight_limit = n * n, density = 1;

    vector<pair<int, int>> *graph = new vector<pair<int, int>>[n];

    int threshold = weight_limit / density;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            int prob = rand() % weight_limit;

            if (prob < threshold)
            {
                int randwt = rand() % weight_limit + 1;
                graph[i].push_back({j, randwt});
                graph[j].push_back({i, randwt});
            }
        }
    }

    return graph;
}

vector<vector<int>> generate_population(int n)
{
    int req_pop_no;
    cout << "\n enter the population count u want ?  -> \t";
    cin >> req_pop_no;

    vector<int> vec;
    for (int i = 1; i < n; i++)
    {
        vec.push_back(i);
    }

    int cnt = req_pop_no;
    vector<vector<int>> population;

    do
    {
        rotate(vec.begin(), vec.begin() + 3, vec.end());
        population.push_back(vec);
        cnt--;
    } while (cnt > 0 && next_permutation(vec.begin(), vec.end()));

    return population;
}

void display_population(const vector<vector<int>> &graph, const vector<vector<int>> &population)
{
    int n = population.size();
    int m = population[0].size();

    for (int i = 0; i < n; i++)
    {
        cout << "\n gene : \t";
        for (int j = 0; j < m; j++)
        {
            cout << population[i][j] << ' ';
        }
        cout << "\t " << fitness_value(population[i]);
    }

    cout << "\n\n";
}

int fitness_value(const vector<int> &person)
{
    int fvalue = 0;
    int geneLength = person.size();

    fvalue = graph[0][person[1]] + graph[0][person[geneLength - 1]];

    for (int i = 0; i < geneLength - 1; i++)
    {
        fvalue += graph[person[i]][person[i + 1]];
    }

    return fvalue;
}