#include "bits/stdc++.h"
#define ll long long int
#define fr(a, b) for(int i = a; i < b; i++)
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

ll power(ll a, ll b) {
    if(b == 0) return 1;
    ll ans = power(a,b/2);
    ans *= ans;
    ans %= MOD;
    if(b % 2){
        ans *= a;
    }
    return ans % MOD;
}

void print(vector<int> v, int start = 0) {
    for(int i = start; i < v.size(); i++) cout << v[i] << " ";
    cout << endl;
}

void Solve() {
    map<int, int> m;
    m.insert({1, 1});
    m.insert({-1, 5});
    for(auto i : m) cout << i.first << " " << i.second << nline;
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

