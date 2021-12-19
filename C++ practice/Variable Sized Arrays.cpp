/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 17-Feb-20             #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double

int main()
{   
    LL n,q;
    LL arr[1000][1000];
    cin>>n>>q;
    for(LL i=0; i<n; i++)
    {
		LL a;
		cin>>a;
		for(LL j=0; j<a; j++)
		cin>>arr[i][j];
		
	}
	
	LL arr2[1000];
	LL arr3[1000];
	
	for(LL i=0; i<q; i++)
	{
		cin>>arr2[i];
		cin>>arr3[i];
	}
	for (LL i=0;i<q;i++)
	{
		cout<<arr[arr2[i]][arr3[i]]<<endl;
		
	}
    
    
    return 0;
}

