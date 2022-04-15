#include<stdio.h>
#include<stdlib.h>
#include<math.h>

/*
Q3. Try some nested calls sqrt(pow(2,abs(x))), putchar(toupper(ch)) etc
*/

int main()
{
	int x = 4, y;
	char ch = 'a';
	y = sqrt(pow(2,abs(x)));// abs is like mode |x|
	printf("sqrt,pow,abs : %d\n", y);

	putchar(toupper(ch));
	printf("\n");

	return 0;
}
