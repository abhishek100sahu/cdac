#include<stdio.h>

/*
Q1. WAP to Convert from one type of pointer/address to other using void*
*/

int main()
{
	int a = 10;
	float b = 3.1415827;	
	void* x = &a;
	
	printf("%d\n", *(int*)x);
	
	x = &b;	

	printf("%f\n", *(float*)x);

	return 0;
}
