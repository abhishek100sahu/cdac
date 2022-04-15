#include<stdio.h>

int main()
{
	union Data
	{
	char gender;
	int prn;
	};
	union Data un;
	
	printf("Enter gender : ");
	scanf("%x", un.gender);

	printf("Enter prn : ");
	scanf("%x", un.prn);

	printf("gender : %x\n", un.gender);
	printf("prn : %x\n", un.prn);

	return 0;
}
