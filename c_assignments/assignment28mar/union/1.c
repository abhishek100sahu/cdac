#include<stdio.h>

/*
Q1. Try the following code
union A
{
int x;
int y;
char ch;
};
union A a1;
a1.x=0x10;
a1.y=0x1121; print a1.x, a1.ch
Calculate size of union , offset of each member
*/
union A
{
	int x;
	int y;
	char ch;
};

int main()
{
	union A a1;
	a1.x = 0x1035;
	printf("%x ",a1.x);
	a1.y = 0x1121;
	printf("%x ",a1.y);

	return 0;
}
