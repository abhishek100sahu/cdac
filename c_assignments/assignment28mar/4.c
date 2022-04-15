/*
Q4. Write a function to swap two variables Pass by reference (Allocate memory on heap)
*/

#include<stdio.h>

int main()
{
	int* ptr1 = malloc(4);
	int* ptr2 = malloc(4);

	*ptr1 = 45;
	*ptr2 = 25;
	
	printf("a : %d\n", *ptr1);
	printf("b : %d\n", *ptr2);

	int temp = *ptr1;
	*ptr1 = *ptr2;
	*ptr2 = temp;

	printf("a : %d\n", *ptr1);
	printf("b : %d\n", *ptr2);

	return 0;
}
