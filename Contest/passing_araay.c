#include<stdio.h>

int main()
{
    int ar[]={2,3,4};
    char ss='s';
    sum(ar,ss);
}
int sum(int ar[], char* ss)
{
    int i,s=0;
    for(i=0;i<3;i++)
    {
        s+=ar[i];
    }
    printf("%d",s);
}
