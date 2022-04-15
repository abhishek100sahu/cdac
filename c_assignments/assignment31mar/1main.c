/*

1.Implement calculator using macros(Use three file architecture)
->Write macros in Header file
->Call functions in main file

*/

#include"1.h"

int main()
{
	int x, y, res;

	printf("Enter num1 : ");
	scanf("%d", &x);

	printf("Enter num2 : ");
	scanf("%d", &y);

	add1(&x, &y);
	sub1(&x, &y);
	mul1(&x, &y);
	div1(&x, &y);

	return 0;
}
