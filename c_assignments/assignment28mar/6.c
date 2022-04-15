/*
Q6. WAP to Addition of two arrays(Allocate on heap)
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
	void* a = calloc(4, 5);
	void* b = calloc(4, 5);
	
	for(int i=0; i<5; i++)
	{
		printf("a[%d] : ", i);
		scanf("%d", ((int*)a+i));
	}

	for(int i=0; i<5; i++)
	{		
		printf("b[%i] : ", i);
		scanf("%d", ((int*)b+i));
	}
	
	void* c = calloc(4, 5);
	for(int i=0; i<5; i++)
	{
		*((int *)c + i) = *((int *)a + i) + *((int *)b + i); // *((int *)a + i)
		printf("%d\t", *((int *)c + i));	
	}

	return 0;
}
