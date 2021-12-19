/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 17-Nov-19             #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double

LL divisor(LL a[], LL d, LL sa);
LL divb(LL arr[], LL d, LL sb);

int main()
{
    LL n,m;
    while(cin>>n>>m)
    {
        LL a[n+1],b[m+1];
        for(LL i=0; i<n; i++)
        {
            cin>>a[i];
        }

        for(LL i=0; i<m; i++)
        {
            cin>>b[i];
        }

        sort(a,a+n);
        sort(b,b+m);

        LL tempa=a[n-1];
        LL tempb=b[m-1];
        LL result=0;
        //LL inc=1;
        while(tempa<=tempb)
        {
            LL funa=divisor(a,tempa,n);
            if(funa==0)
            {
                LL funb=divb(b, tempa, m);
                if(funb==0)
                    result++;
            }
            //inc++;
            tempa=tempa+a[n-1];
        }

        cout<<result<<endl;
    }

     return 0;
}

LL divisor(LL a[], LL d, LL sa)
    {
        LL tmp=0;
        for(LL i=0; i<sa; i++)
        {
            if(d%a[i]!=0)
            {
                return 1;
            }
        }

        return 0;

    }

LL divb(LL arr[], LL d, LL sb)
{
    LL tmp=0;
    for(LL i=0; i<sb; i++)
    {
        if(arr[i]%d!=0)
        {
            return 1;
        }
    }

    return tmp;
}
