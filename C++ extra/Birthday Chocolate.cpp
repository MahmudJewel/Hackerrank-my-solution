/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 03/03/20              #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double

int main()
{
	LL n,ar[1000],d,m;
	cin>>n;
	for(LL i=0; i<n; i++)
	{
		cin>>ar[i];
	}
	cin>>d>>m;
	
	LL result=0;
		if(m==1)              ///Critical case
		{
			for(LL i=0; i<n; i++)
			if(ar[i]==d)
			result++;
		}
			
			
	else
	{
	for(LL i=0; i<=n-m; i++)
	{
		LL sum=ar[i];
		LL temp=1;
		
		while(temp<m)
		{
			sum+=ar[i+temp];
			temp++;
			}
			
			if(sum==d)
			result++;
		
		}}
		cout<<result<<endl;
	
	
}
