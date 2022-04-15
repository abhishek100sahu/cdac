#include<stdio.h>

int main()
{
	int a = 256;
	int b = 2;

	int res = (int*)b+a;
	printf("%d\n", res);
	return 0;
}
