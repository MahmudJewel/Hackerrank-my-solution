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
        LL temp;
        for(LL i=0; i<n; i++)
        {
            temp=n-1-i;
            for(LL j=0; j<n;j++)
            {
                if(j==temp)
                {
                    cout<<'#';
                    temp++;
                }
                else
                    cout<<' ';
            }
            cout<<endl;
        }
    }
}
