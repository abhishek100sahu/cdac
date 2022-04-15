#include<stdio.h>

struct employee
{
	int empID;
	char name[100];
	int salary;
	int year;
};

typedef struct employee emp;

void exp(emp* empl,int* n)
{	
	int senior, junior, exper[*n];
	
	for(int i=0; i<*n; i++)
	{
		exper[i] = 2022 - empl[i].year;
	}
		
	for(int i=0; i<*n; i++)
	{
		printf("Name : %s | Experience : %d\n", empl[i].name, exper[i]);
	}	
}



int main()
{
	
	emp em[10];
	int n = 0, i = 0;

	emp *ptr = em;

	printf("Enter no. of epmloyees : ");
	scanf("%d", &n);

	// Taking input from user
	for(int i=0; i<n; i++)
	{
		printf("Enter empID of e%d : ", i+1);
		scanf("%d", &ptr[i].empID);
	
		printf("Enter name of e%d : ", i+1);
		scanf("%s", ptr[i].name);

		printf("Enter salary of e%d : ", i+1);
		scanf("%d", &ptr[i].salary);

		printf("Enter year of joining of e%d : ", i+1);
		scanf("%d", &ptr[i].year);
	}
	printf("\n");
	
	// Printing Employee details
	for(int i=0; i<n; i++)
	{
		printf("e%d : empID | name | salary | year |\n", i+1);
		printf("e%d : %d | %s | %d | %d \n", i+1, ptr[i].empID, ptr[i].name, ptr[i].salary, ptr[i].year);
	}

	// Total salary
	int total=0;
	for(int i=0; i<n; i++)
	{
		total += ptr[i].salary;
	}
	printf("Total salary of Employees : %d\n", total);

	// Average Salary
	int average = 0;
	average	= total/n;
	printf("Average salary of Employee : %d\n", average);

	// Minimum Salary
	int min = ptr[0].salary;
	for(i=0; i<n; i++)
	{
		if(min > ptr[i].salary)
		{
			min = ptr[i].salary;
		}
	}
	printf("Minimum Salary : %d\n", min);

	// Maximum Salary
	int max = ptr[0].salary;
	for(i=0; i<n; i++)
	{
		if(max < ptr[i].salary)
		{
			max = ptr[i].salary;
		}
	}
	printf("Maximum Salary : %d\n", max);

	// Experience of Employee
	exp(ptr, &n);

	return 0;
}
