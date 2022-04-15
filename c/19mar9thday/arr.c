# include<stdio.h>

int main()
{
	int arr[5];
	arr[0] = 10;
	arr[1] = 20;
	arr[2] = 30;
	arr[3] = 40;
	arr[4] = 50;

	printf("arr : %x\n", arr);
	printf("&arr : %x\n", &arr);
	printf("arr : %x\n", *arr);
	printf("&arr[0] : %x\n", &arr[0]);
	printf("&arr[1] : %x\n", &arr[1]);
	printf("*&arr : %x\n", *&arr);
	return 0;
}
