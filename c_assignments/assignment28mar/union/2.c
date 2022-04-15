#include<stdio.h>
#include<stdlib.h>

/*
Q2. Analyse the following code
union A
{
int x;
float y;
double z;
int arr[2];
}a1;
a1.y=6.25f;
printf(“x=%x\n”,a1.x);
a1.z=0.15625;;
printf(“%x%x\n”,a1.arr[1],a1.arr[0]);

*/
union A
{
	int x;
	float y;
	double z;
	int arr[2];
} a1;

int main()
{
	a1.x = 3;
	printf("x = %x\n", a1.x);
	a1.y = 6.25f;
	printf("y = %f\n",a1.y);
	a1.z=0.15625;
	
	printf("sizeof(a1) 😂️: %d\n", sizeof(a1));

	printf("Num1 😋️: ");
	scanf("%d", &a1.arr[0]);
	printf("arr[0] : %d\n", a1.arr[0]);

	printf("Num2 😋️: ");
	scanf("%d", &a1.arr[1]);
	printf("arr[0] : %d\n", a1.arr[1]);

	return 0;
}
