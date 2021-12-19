/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 19-Jun-19             #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double

LL divisible_sum_pair(LL arr[], LL siz, LL k);
int main()
{
    LL n,k;
    while(cin>>n>>k)
    {
        LL arr[n+1];
        for(LL i=0; i<n; i++)
            cin>>arr[i];

        LL result=divisible_sum_pair(arr,n,k);
        cout<<result<<endl;
    }

     return 0;
}


LL divisible_sum_pair(LL arr[], LL siz, LL k)
{
    LL ans=0;
    for(LL i=0; i<siz-1; i++)
    {
        for(LL j=i+1; j<siz; j++)
        {
            LL temp=arr[i]+arr[j];
            if(temp%k==0)
                ans++;
        }
    }
    return ans;
}
