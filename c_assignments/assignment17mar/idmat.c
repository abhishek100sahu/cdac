#include<stdio.h>

int main()
{
	int arr[10][10];
	int y, r, c, i, j;

	printf("Enter the name of rows : ");
	scanf("%d", &r);
	printf("Enter the number of column : ");
	scanf("%d", &c);

	for(i=0; i<r; i++)
	{
		for(j=0; j<c; j++)
		{
			printf("Enter arr[%d][%d] : ", i, j);
			scanf("%d", &arr[i][j]);
		}
	}

	for(i=0; i<r; i++)
	{
		for(j=0; j<c; j++)
		{
			if(arr[i][j] != 1 && arr[i][j] != 0)
			{
				y = 0;
				break;
			}
		}
	}

	if(y = 1)
		printf("It's an identity Matrix");
	else
		printf("It's not an Identity matrix");

	return 0;
}
