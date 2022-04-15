#include<stdio.h>

int main()
{
	struct student{
		int prn;
		char name[100];
		char phone[12];
	};

	struct student std[100];
	
	for(int i=0; i<2; i++)
	{
		// Input user for s1
		printf("Enter prn of std[%d] : ", i);
		scanf("%d", &std[i].prn);
		
		printf("Enter name of std[%d] : ", i);
		scanf("%s", std[i].name);
		
		printf("Enter phone no. of std[%d] : ", i);
		scanf("%s", std[i].phone);
		
	}

	for(int i=0; i<2; i++)
	{
		printf("std[%d] : %d|%s|%s\n", i, std[i].prn, std[i].name, std[i].phone);
	}

	return 0;
}

