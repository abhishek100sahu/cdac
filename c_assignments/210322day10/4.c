#include<stdio.h>
/*
Q4. Whats wrong in this code, any fixes to the problem?
int* test(int x)
{
int y=x*x;
return &y;
}
*/
int test(int x)
{
		int y = x * x;
		y;
		return y;
}

int main()
{
	int y = 2;
	int z = test(y);

	printf("%d\n", z);

	return 0;
}
