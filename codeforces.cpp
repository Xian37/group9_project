
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int n;
    cin>>n;
    while(n){
        int na;
        cin>>na;
        vector <int> ar(na);
        for(int i=0;i<na;i++){
            cin>>ar[i];
        }
        sort(ar.begin(),ar.end());
        vector <int> ans;
        ans.push_back(ar[0]);
        ans.push_back(ar[1]);
        ans.push_back(ar[na-1]);
        ans.push_back(ar[na-2]);
        int sum=2*(ans[3]+ans[2]-ans[1]-ans[0]);
        cout<<sum<<endl;
        
        
        n--;
    }

    return 0;
}

