#include<stdio.h>

// 1.Write a program to caculate the sum of n numbers(Use static varaibles)

void add()
{
	static int x = 0;
	static int sum = 0;
	x++;
	sum += x;
	
	printf("Sum : %d\n", sum);
}

int main()
{
	int x;

	printf("Enter number : ");
	scanf("%d", &x);

	for(int i=0; i<x; i++)
	{
		add();
	}

	return 0;
}
