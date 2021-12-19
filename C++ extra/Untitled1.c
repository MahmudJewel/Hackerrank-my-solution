#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int Sum(int a, int b)
{
    return a+b;
}
int Sub(int a, int b)
{
    return a-b;
}

float Sumf(float c, float d)
{
    return c+d;
}
float Subf(float c, float d)
{
    return c-d;
}


int main()
{
	int a,b,r1,r2;
    float c,d,r3,r4;
    scanf("%d %d %f %f",&a,&b,&c,&d);
    r1=Sum(a,b);
    r2=Sub(a,b);
    r3=Sumf(c,d);
    r4=Subf(c,d);
    printf("%d %d\n",r1,r2);
    printf("%.1f %.1f\n",r3,r4);

    return 0;
}


