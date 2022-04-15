#include"employee.h"
#include<stdio.h>

// Menu
int menu()
{
	int button = 0;	
	printf("\nPress [1] : add Employee\n");
	printf("Press [2] : Display Employee\n");
	printf("Press [3] : Search Employee\n");
	printf("Press [4] : Change Employee Name\n");
	printf("Press [5] : Exit\n");
	scanf("%d", &button);

	return button;
}
// taking Employee details
void input(employee* arr, int* n)
{	// name
	printf("Enter Name : ");
	scanf("%s", arr[*n].name);
	// empID
	printf("Enter empId : ");
	scanf("%d", &arr[*n].empId);
	// Date of Birth
	printf("Enter Date of Birth\n");
	printf("Day : ");
	scanf("%d", &arr[*n].dob.dd);
	printf("Month : ");
	scanf("%d", &arr[*n].dob.mm);
	printf("Year : ");
	scanf("%d", &arr[*n].dob.yyyy);
	// Address
	printf("Enter the Address\n");
	printf("flatNo : ");
	scanf("%d", &arr[*n].ad.flatNo);
	printf("city : ");
	scanf("%s", arr[*n].ad.city);
	printf("state : ");
	scanf("%s", arr[*n].ad.state);

	++(*n);
}

// Providing Employee details
void display(employee* arr, int* n)
{
	for(int i=0; i<*n; i++)
	{
		printf("Name : %s | ",arr[i].name);
		printf("empId : %d | ",arr[i].empId);
		printf("DD : %d | ",arr[i].dob.dd);
		printf("MM : %d | ",arr[i].dob.mm);
		printf("YYYY : %d | ",arr[i].dob.yyyy);
		printf("flatNo : %d | ",arr[i].ad.flatNo);
		printf("city : %s | ",arr[i].ad.city);
		printf("state : %s | ",arr[i].ad.state);
		printf("\n");
	}
}

// Searching employee be empId
void search(employee* arr, int* n)
{	
	int id;
	printf("Enter the empId : ");
	scanf("%d", &id);
	
	for(int i=0; i<*n; i++)
	{
		if(arr[i].empId == id)
		{
			printf("\nName : %s | ",arr[i].name);
			printf("empId : %d | ",arr[i].empId);
			printf("DD : %d | ",arr[i].dob.dd);
			printf("MM : %d | ",arr[i].dob.mm);
			printf("YYYY : %d | ",arr[i].dob.yyyy);
			printf("flatNo : %d | ",arr[i].ad.flatNo);
			printf("city : %s | ",arr[i].ad.city);
			printf("state : %s | ",arr[i].ad.state);
			printf("\n");
		}
	}
}

// Updating employee name
void change(employee* arr, int* n)
{
	int id;
	printf("Enter the empId : ");
	scanf("%d", &id);

	for(int i=0; i<*n; i++)
	{
		if(arr[i].empId == id)
		{
			printf("Updated name : ");
			scanf("%s", arr[i].name);
			printf("Update Succesfully!");						
		}
	}
}

