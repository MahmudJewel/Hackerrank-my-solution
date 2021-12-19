/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 18-nov-19             #                                  *
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
		LL game[n+1];
		for(LL i=0; i<n; i++)
		{
			cin>>game[i];
		}
		
		LL min=game[0];
		LL max=game[0];
		LL c1=0,c2=0;
		for(LL i=1;i<n; i++)
		{
			if(min>game[i])
			{
				min=game[i];
				c2++;
			}
			
			if(max<game[i])
			{
				max=game[i];
				c1++;
			}
		}
		
		cout<<c1<<" "<<c2<<endl;
		
	}
     return 0;
}
