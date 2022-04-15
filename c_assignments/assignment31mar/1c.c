#include"1mac.h"
#include<stdio.h>


int add1(int* x, int* y)
{
	printf("Sum : %d\n", add(*x, *y));
}

int sub1(int* x, int* y)
{
	printf("sub : %d\n", sub(*x, *y));
}

int mul1(int* x, int* y)
{
	printf("mul : %d\n", mul(*x, *y));
}

int div1(int* x, int* y)
{
	if(*x > *y)
		printf("div : %d\n", div(*x, *y));
}
