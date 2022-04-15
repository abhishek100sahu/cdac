#include<stdio.h>

int main()
{
	struct student{
		int prn;
		char name[100];
		char phone[12];
		int no_of_assignment;
	};

	struct student s1;
	struct student s2;

	// Input user for s1
	printf("Enter prn os s1 : ");
	scanf("%d", &s1.prn);
	
	printf("Enter name of s1 : ");
	scanf("%s", s1.name);
	
	printf("Enter phone no. of s1");
	scanf("%s", s1.phone);
	
	printf("Enter no. of assignment of s1 : ");
	scanf("%d", &s1.no_of_assignment);

	// Input user for s2
	printf("Enter prn os s1 : ");
	scanf("%d", &s2.prn);
	
	printf("Enter name of s1 : ");
	scanf("%s", s2.name);
	
	printf("Enter phone no. of s1");
	scanf("%s", s2.phone);
	
	printf("Enter no. of assignment of s1 : ");
	scanf("%d", &s2.no_of_assignment);

	// Printing details

	printf("s1 -> %d | %s | %s | %d \n", s1.prn, s1.name, s1.phone, s1.no_of_assignment);
	printf("s2 -> %d | %s | %s | %d \n", s2.prn, s2.name, s2.phone, s2.no_of_assignment);

	return 0;
}
