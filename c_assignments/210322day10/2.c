#include<stdio.h>

/*
Q2. Write a function to swap two variables using Pass by value, Pass by
reference
*/
void swap_val(int x, int y)
{
	int temp = x;
	x = y;
	y = temp;

	printf("After | Value | a : %d b : %d\n", x, y);
}

void swap_ref(int* x, int* y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

int main()
{
	int a =10;
	int b = 20;

	printf("Before | a : %d b : %d\n", a, b);
	swap_ref(&a, &b);
	printf("After | Reference | a : %d b : %d\n", a, b);
	swap_val(a, b);
	
	
	return 0;
}
