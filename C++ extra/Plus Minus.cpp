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
        LL arr[n+1];
        D p=0,m=0,z=0,rp,rm,rz;
        for(LL i=0; i<n; i++)
        {
            cin>>arr[i];

        }
        for(LL i=0; i<n; i++)
        {
            if(arr[i]>0)
                p++;
            else if(arr[i]<0)
                m++;
            else
                z++;
        }
        //cout<<p<<" "<<m<<" "<<z<<endl;
        D c=D(n);

        rp=p/c;
        rm=m/c;
        rz=z/c;
        printf("%.6lf\n%.6lf\n%.6lf\n",rp, rm,rz);
        //cout<<rp<<endl;

    }
    return 0;
}
