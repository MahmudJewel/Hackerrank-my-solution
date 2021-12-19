/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 07/01/19              #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double

int main()
{
    LL arr[6],max=0,min=6000000000;
    for(LL i=0; i<5; i++)
    {
        cin>>arr[i];
    }

    for(LL i=0; i<5; i++)
    {
        LL temp=0;
        for(LL j=0; j<5; j++)
        {
            if(i==j)
                continue;
            else
            {
                temp+=arr[j];
            }
        }
        if(temp>max)
            max=temp;
        if(temp<min)
            min=temp;
    }
    cout<<min<<' '<<max<<endl;

    return 0;
}
