#include<stdio.h>

#define add(arg1, arg2) arg1+arg2
#define sub(arg1, arg2) arg1-arg2
#define mul(arg1, arg2) arg1*arg2
#define div(arg1, arg2) arg1/arg2

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

int main()
{
	int x, y, res;

	printf("Enter num1 : ");
	scanf("%d", &x);

	printf("Enter num2 : ");
	scanf("%d", &y);

	add1(&x, &y);
	sub1(&x, &y);
	mul1(&x, &y);
	div1(&x, &y);

	return 0;
}
