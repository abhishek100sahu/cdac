#include<stdio.h>

int main()
{
	struct student
	{
		int prn;
		unsigned age : 4;
	};
		
	struct student s1;
	s1.age = 0xF;

	printf("%d\n", s1.age);

	return 0;
}
