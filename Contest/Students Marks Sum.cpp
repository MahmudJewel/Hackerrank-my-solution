/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 20/06/19              #                                  *
*****************##################################************************************************/

#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define S string
#define D double


main()
{
  LL n;
  while(cin>>n)
  {
      LL ar[n];
      S s;
      LL sum=0;
      for(LL i=0;i<n;i++)
      {
          cin>>ar[i];
      }

      cin>>s;
      if(s=="b")
      {
      for(LL i=0;i<n;i++)
      {
          sum=sum+ar[i];
          i++;
      }
      }
      else
        {
      for(LL i=1;i<n;i++)
      {
          sum=sum+ar[i];
          i++;
      }
      }

      cout<<sum<<endl;

  }
}
