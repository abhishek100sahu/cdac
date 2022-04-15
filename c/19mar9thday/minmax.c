# include<stdio.h>

int main()
{
	int arr[5] ={1, 2, 3, 4, 5};
	int sum = 0;
	int avg, min=0, max, a, b;
	int length = sizeof(arr)/sizeof(*arr+0);

	// Sum
	for(int i=0; i<length; i++)
	{
		sum += *(arr+i);
	}
	
	printf("Sum : %d\n", sum);

	// Average
	avg = sum/length;

	printf("Average : %d\n", avg);
	
	// Minimum
	a = *(arr+1);// Coping the element of 0th index in a
	for(int i=0; i<length; i++)
	{
		if(*(arr+i) < a)
		{
			min = *(arr+i);
		}
	}
	printf("Min : %d\n", min);

	// Maximum
	b = *(arr+0);// Coping the element of 0th index in a
	for(int i=0; i<length; i++)
	{
		if(*(arr+i) > b)
		{
			max = *(arr+i);
		}
	}
	printf("Min : %d\n", max);


	return 0;
}
