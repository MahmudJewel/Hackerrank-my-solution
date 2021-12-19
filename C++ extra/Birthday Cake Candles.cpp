/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 01-Jun-19             #                                  *
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
        LL arr[n+1];
        for(LL i=0; i<n; i++)
            cin>>arr[i];

         LL temp=1;
        sort(arr,arr+n);
        for(LL i=n-2; i>=0; i--)
        {
            if(arr[i]==arr[n-1])
                temp+=1;
            else
                break;
        }
        cout<<temp<<endl;
    }

     return 0;
}
