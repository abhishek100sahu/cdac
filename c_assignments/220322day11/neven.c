#include<stdio.h>

// 7.Write a program to print n even numbers(take n input from user)

void prime(int* num)
{
	for(int i=1; i<=*num; i++)
	{
		int b = i * 2;
		printf("%d ", b);
	}
	printf("\n");
}

int main()
{
	int num;

	printf("Enter no. : ");
	scanf("%d", &num);
	prime(&num);

	return 0;
}
