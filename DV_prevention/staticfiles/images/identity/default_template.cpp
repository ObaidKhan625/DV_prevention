#include "bits/stdc++.h"
#define ll long long int
#define frn(a, b) for(int i = a; i < b; i++)
#define nline "\n"

using namespace std;

const int MOD=1000000007;

#define deb(...) logger(#__VA_ARGS__, __VA_ARGS__)
template<typename ...Args>
void logger(string vars, Args&&... values) {
    cout << vars << " = ";
    string delim = "";
    (..., (cout << delim << values, delim = ", "));
    cout << nline;
}

ll power(ll x, ll y)
{
    ll res = 1;
    x = x % MOD; 
    if (x == 0) return 0;
    while (y > 0)
    {
        if (y & 1)
            res = (res*x) % MOD;
        y = y>>1;
        x = (x*x) % MOD;
    }
    return res;
}

void print_array(auto arr[], int n) {
    for(int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << "\n";
}

void print_vector(vector<int> v) {
    int n = v.size();
    for(int i = 0; i < n; i++) cout << v[i] << " ";
    cout << "\n";
}

void Solve() {
    int n;
    cin >> n;
    ll arr[n];
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
        cout << arr[i] << " ";
    }
    cout << nline;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--)
    Solve();
    return 0;
}

