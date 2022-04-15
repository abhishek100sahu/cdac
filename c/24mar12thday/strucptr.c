#include<stdio.h>

int main()
{
	struct student{
		int prn;
		char name[100];
		int assign;
		// 108 bytes of memory
	};

	struct student s1;
	struct student s2;

	struct student* pt = &s1;

	// Input from user
	printf("Enter prn of s1 : ");
	scanf("%d", &pt->prn);
	
	printf("Enter name of s1 : ");
	scanf("%s", pt->name);
	
	printf("Enter phone no. of s1 : ");
	scanf("%d", &pt->assign);

	// Input from user
	printf("Enter prn of s2 : ");
	scanf("%d", &s2.prn);
	
	printf("Enter name of s2 : ");
	scanf("%s", s2.name);
	
	printf("Enter phone no. of s2 : ");
	scanf("%d", &s2.assign);

	printf("s1 -> %d | %s | %d \n", s1.prn, s1.name, s1.assign);
	printf("s2 -> %d | %s | %d \n", s2.prn, s2.name, s2.assign);
	
	printf("s1 -> prn : %d\n", (*pt).prn);
	printf("s1 -> name : %s\n", (*pt).name);
	printf("s1 -> assing : %d\n", (*pt).assign);

	printf("s2 -> prn : %d\n", pt->prn);
	printf("s2 -> name : %s\n", pt->name);
	printf("s2 -> assing : %d\n", pt->assign);		

	return 0;
}
