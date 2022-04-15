/*
Write a single function to return sum, product of two no.s
*/

#include<stdio.h>

int sum(int* x, int* y, int* s, int* product)
{
	*s = *x + *y;

	*product = *x * *y;
	
}

int main()
{
	int a = 111;
	int b = 3;
	int product=1, s=0;

	sum(&a, &b, &s, &product);
	
	printf("Sum is : %d\n", s);
	printf("Product is : %d\n", product);

	return 0;
}	
