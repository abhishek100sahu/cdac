/*
Q2. WAP to Test arithmetic operation on void pointers
*/

#include<stdio.h>

int main()
{
	float a = 650.5;
	int b = 20;

	void* p = &a;
	void* q = &b;
	
	float r = *((float*)p) * *((int*)q);
	
	printf("Multiplication : %f\n", r);

	return 0;
}

/*
Void pointer are working fine with integer & all the general operations are being performed, however in case of float typecasting we're unable to  perform any type of operations
*/
