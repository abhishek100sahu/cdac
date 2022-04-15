#include<stdio.h>

void square(int* x)
{
	printf("Square : %d\n", (*x)*(*x));
}

int main()
{
	int* x =malloc(sizeof(int));
	printf("Enter num : ");
	scanf("%d", x);
	
	square(x);

	printf("Data : %d", *x);
	free(x);

	return 0;
}
