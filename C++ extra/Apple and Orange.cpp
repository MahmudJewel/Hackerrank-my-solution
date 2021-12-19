/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 02-Jun-19             #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double


int main()
{
    LL s,t;
    while(cin>>s && cin>>t)
    {
        LL a,b,m,n;
        cin>>a>>b>>m>>n;
        LL apple[m+1],orange[n+1],ap=0,orr=0;
        for(LL i=0; i<m; i++)
            cin>>apple[i];

        for(LL i=0; i<n; i++)
            cin>>orange[i];

                LL temp;
            for(LL i=0; i<m; i++)
            {
                temp=apple[i]+a;
                if(temp>=s && temp<=t)
                    ap+=1;
            }

            for(LL i=0; i<n; i++)
            {
               temp=orange[i]+b;
                if(temp>=s && temp<=t)
                    orr+=1;
            }

            cout<<ap<<endl<<orr<<endl;
    }

 return 0;
}
