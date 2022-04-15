#include<stdio.h>

int main()
{
	auto int a = 10;
	printf("a : %d\n", a);
	printf("address of a : %x\n", &a);
	printf("size of a : %d\n", sizeof(a));

	register int b = 10;
	printf("b : %d\n", b);
	// printf("address of b : %x\n", &b);
	printf("size of b : %d\n", sizeof(b));

	return 0;
}
