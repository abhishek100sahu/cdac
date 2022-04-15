#include<stdio.h>

int arr[8];
int main()
{
	int x = 64, a = 0, b;
	int y = x;
	int z = x;
	int length = sizeof(arr)/4;
	int flag = 0;

	for(int i=0; i<length; i++)
	{
		a = x % 2;
		x /= 2;
		*(arr+i) = a;
	}
	
	printf("Binary : ");
	for(int i=length; i>0; i--)
	{	if(flag == 0)
		{
			printf("%d", *(arr+i));
			flag = 1;
		}
		else
			break;	
	}
	printf("\n");
	
	for(int i=0; i<length; i++)
	{
		a = y % 8;
		y /= 8;
		*(arr+i) = a;
	}
	
	
	printf("Octal : ");
	for(int i=length; i>0; i--)
	{
		printf("%d", *(arr+i));	
	}
	printf("\n");

	for(int i=0; i<length; i++)
	{
		a = z % 16;
		z /= 16;
		*(arr+i) = a;
	}
	
	
	printf("Hexadecimal : ");
	for(int i=length; i>0; i--)
	{
		printf("%d", *(arr+i));	
	}
	printf("\n");
	
	return 0;
}	

