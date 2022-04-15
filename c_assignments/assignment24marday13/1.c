#include<stdio.h>

//Q1.Create a Employee structure to store the EMPID,NAME,Phone,Email,Salary.(Use array of structure)

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
	emp em[10];

	// Taking input from user
	for(int i=0; i<2; i++)
	{
		printf("Enter empID of e%d : ", i+1);
		scanf("%d", &em[i].empID);
	
		printf("Enter name of e%d : ", i+1);
		scanf("%s", em[i].name);

		printf("Enter phone of e%d : ", i+1);
		scanf("%s", em[i].phone);

		printf("Enter email of e%d : ", i+1);
		scanf("%s", em[i].email);

		printf("Enter salary of e%d : ", i+1);
		scanf("%d", &em[i].salary);
	}

	// Printing Employee details
	for(int i=0; i<2; i++)
	{
		printf("e%d : empID | name | phone | email | salary\n", i);
		printf("e%d : %d | %s | %s | %s | %d \n", i+1, em[i].empID, em[i].name, em[i].phone, em[i].email, em[i].salary);
	}

	return 0;
}
