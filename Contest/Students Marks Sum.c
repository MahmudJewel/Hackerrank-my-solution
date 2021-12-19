/****************##################################*************************************************
*                #   Editor : Jewel Mahmud        #                                  *
*                #   CSE 13th, MBSTU              #                                  *
*                #   Date : 20/06/19              #                                  *
*****************##################################************************************************/

#include<stdio.h>
#define LL long long
#define S string
#define D double
void marks_summation(LL ar[],char* s,LL n);

int main()
{
   LL n;
  while((scanf("%lld",&n))==1)
  {
      LL ar[n],i;
      char s;

      for(i=0;i<n;i++)
      {
          //cin>>ar[i];
          scanf("%lld",&ar[i]);
      }
      getchar();
      scanf("%c",&s);

      marks_summation(ar,s,n);
  }
  return 0;
}

void marks_summation(LL ar[],char *s,LL n)
{
   // printf("%c",s);
    LL i,sum=0;

      if(s=='b')
      {
          //printf("Hello\n");
      for(i=0;i<n;i++)
      {
          //printf("%lld\n",sum);
          sum=sum+ar[i];
          i++;

      }
      }
      else
        {
      for(i=1;i<n;i++)
      {
          sum=sum+ar[i];
          i++;
      }
      }

      printf("%lld\n",sum);

  }
