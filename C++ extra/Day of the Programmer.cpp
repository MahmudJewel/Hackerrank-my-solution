/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 20-Jun-19             #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double

bool leapyear(LL y);
int main()
{
    LL y;
    while(cin>>y)
    {
        LL d;
        if(y==1918)
        {
           cout<<26<<'.'<<"09"<<'.'<<y<<endl;
        }
        else
        {
            bool a=leapyear(y);
            if(a==true)
                d=12;
            else
                d=13;
            cout<<d<<'.'<<"09"<<'.'<<y<<endl;
        }

    }

    return 0;
}

bool leapyear(LL y)
{
    if(y<1918 && y%4==0)
            return true;
    else if(y%400==0 ||(y%4==0 && y%100!=0))
        return true;
    else
        return false;
}
