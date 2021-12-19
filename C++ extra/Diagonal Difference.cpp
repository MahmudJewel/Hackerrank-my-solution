/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 06/02/19              #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double


int main()
{
    LL n;
    while(cin>>n)
    {
        if(n<0)
            n=-n;
            LL a=n+1;
        LL arr[a][a],sum1=0,sum2=0;
        for(LL i=0; i<n;i++)
        {
            for(LL j=0; j<n;j++)
            {
                cin>>arr[i][j];
            }
        }

        for(LL i=0; i<n; i++)
        {
            sum1+=arr[i][i];
            sum2+=arr[i][n-1-i];
        }

        if(sum1>sum2)
            cout<<sum1-sum2<<endl;
        else
            cout<<sum2-sum1<<endl;
    }
    return 0;
}
