#include<stdio.h>
#include<stdlib.h>

int* square(int* x)
{
	int* y = malloc(4);
	*y = (*x)*(*x);
	
	return y;
}

int main()
{
	int *x = malloc(sizeof(int));
	
	printf("Enter the num : ");
	scanf("%d", x);
	printf("Data : %d", *x);

	int* y = square(x);
	printf("Square : %d", *y);
	free(x);

	return 0;
}
