/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 03-Jun-19             #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double

///time limit.
int main()
{
    LL x1,x2,v1,v2;
    while(cin>>x1>>v1>>x2>>v2)
    {
        if((x1<x2 && v1<v2) || (x1>x2 && v1>v2))
            cout<<"NO"<<endl;  ///if one is less & speed is less, they never meet.

        else
        {
            if(x1>x2)
            {
                while(x1>x2)
                {
                    x1+=v1;
                    x2+=v2;
                }
            }

            else
            {
                while(x1<x2)
                {
                    x1+=v1;
                    x2+=v2;
                }

            }
            if(x1==x2)
                cout<<"YES"<<endl;
            else
                cout<<"NO"<<endl;

        }

    }

    return 0;
}
