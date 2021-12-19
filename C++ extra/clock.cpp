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
    S date; ///01:02:12
    while(cin>>date)
    {
        S demo="";
        demo=date;


        if(date[8]=='A' || date[8]=='a')
        {
            if(date[1]=='2' && date[0]=='1')
               {
                   demo[0]='0';
                   demo[1]='0';
               }

            for(LL i=0; i<8; i++)
                cout<<demo[i];
                cout<<endl;
        }

        else
        {
            LL h,m,s;
        h=date[0]-'0';
        h=h*10+date[1]-'0';
        //cout<<h<<endl;
        /*m=date[3]-'0';
        m=m*10+date[4]-'0';
        s=date[6]-'0';
        s=s*10+date[7]-'0';*/

        if(h==12)
        {
            //cout<<h;
            for(LL i=0; i<8; i++)
                cout<<date[i];
            cout<<endl;
        }
        else
        {
            cout<<h+12;
            for(LL i=2; i<8; i++)
                cout<<date[i];
            cout<<endl;
        }
        }



    }
     return 0;
}
