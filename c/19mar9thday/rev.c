#include<stdio.h>

int main()
{
	int arr[5];
	int length = sizeof(arr)/sizeof(*(arr+0));
	int start = 0, end = length;

	// Input
	for(int i=0; i<length; i++)
	{
		printf("Enter array no. : ");
		scanf("%d", arr+i);
	}

	while(start > end)
	{
		int temp = *(arr+start);
		*(arr+start) = *(arr+end);
		*(arr+start) = temp;
		start++;
		end--;
	}

	for(int i=0; i<length; i++)
	{
		printf("%d\n", *(arr+i));	
	}

	return 0;
}
