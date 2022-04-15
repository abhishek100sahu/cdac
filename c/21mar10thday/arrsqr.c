#include<stdio.h>

void square(int* x)// taking input pointer pointing to 1st arr address
{
	for(int i=0; i<1; i++)// here incrementing 4 bytes of address
	{
		x[i] = x[i] * x[i];
		// *(x + i) = *(x + i) * *(x + i)
	}
}

void square1(int* x)// taking input pointer pointing to 1st arr address
{
	for(int i=1; i>=0; i--)// here decrementing 4 bytes of address
	{
		// x[i] = x[i] * x[i];
		// *(x - i) = *(x - i) * *(x - i)
		*(x - i) = *(x - i) * *(x - i);
	}
}

int main()
{
	int arr[5] = {10, 20, 30, 40, 50};
	square1(&arr+1);
	// parameter 1000|address of 1st block of arr
	for(int i=0; i<5; i++)
	{
		printf("%d\n", arr[i]);
	}

	return 0;
}
		
