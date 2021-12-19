/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 16-nov-19             #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double


int main()
{
	LL test;
	cin>>test;
	while(test--)
	{
		LL grade;
		cin>>grade;
		if(grade<38)
		cout<<grade<<endl;
		else
		{
			if(grade%5==4)
			cout<<grade+1<<endl;
			else if (grade%5==3)
			cout<<grade+2<<endl;
			else
			cout<<grade<<endl;
		}
	}

     return 0;
}
