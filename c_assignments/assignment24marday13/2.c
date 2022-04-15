#include<stdio.h>

int main()
{
	struct employee
	{
		int empID;
		char name[100];
		char phone[10];
		char email[20];
		int salary;
	};

	typedef struct employee emp;
	emp e1;
	emp e2;

	emp *ptr1 = &e1;
	emp *ptr2 = &e2;
	

	// Taking input from user
	printf("Enter empID of e1 : ");
	scanf("%d", &ptr1->empID);

	printf("Enter name of e1 : ");
	scanf("%s", ptr1->name);

	printf("Enter phone of e1 : ");
	scanf("%s", ptr1->phone);

	printf("Enter email of e1 : ");
	scanf("%s", ptr1->email);

	printf("Enter salary of e1 : ");
	scanf("%d", &ptr1->salary);

	// Printing Employee details of e1
	printf("e1 : empID | name | phone | email | salary\n");
	printf("e1 : %d | %s | %s | %s | %d \n", ptr1->empID, ptr1->name, ptr1->phone, ptr1->email, ptr1->salary);

	// Taking input from user for e2
	printf("Enter empID of e2 : ");
	scanf("%d", &ptr2->empID);

	printf("Enter name of e2 : ");
	scanf("%s", ptr2->name);

	printf("Enter phone of e2 : ");
	scanf("%s", ptr2->phone);

	printf("Enter email of e2 : ");
	scanf("%s", ptr2->email);

	printf("Enter salary of e2 : ");
	scanf("%d", &ptr2->salary);

	// Printing Employee details of e1
	printf("e2 : empID | name | phone | email | salary\n");
	printf("e2 : %d | %s | %s | %s | %d \n", ptr2->empID, ptr2->name, ptr2->phone, ptr2->email, ptr2->salary);

	return 0;
}
