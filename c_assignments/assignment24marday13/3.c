#include<stdio.h>

struct student
{
	int stdID;
	char name[100];
	char phone[10];
	char email[20];
	int mark[3];		
};

int main()
{
	typedef struct student std;
	
	std st[10];

	std *ptr = st;

	// Taking input from user
	for(int i=0; i<2; i++)
	{
		printf("Enter stdID of e%d : ", i+1);
		scanf("%d", &ptr[i].stdID);
	
		printf("Enter name of e%d : ", i+1);
		scanf("%s", ptr[i].name);

		printf("Enter phone of e%d : ", i+1);
		scanf("%s", ptr[i].phone);

		printf("Enter email of e%d : ", i+1);
		scanf("%s", ptr[i].email);

		for(int j=0; j<3; j++)
		{
			printf("Enter marks of e%d in subject%d : ", i+1, j+1);
			scanf("%d", &ptr[i].mark[j]);
		}
	}

	int total[3],sum=0, phy=0, chem=0, mat=0;
	for(int i=0; i<2; i++)
	{
		for(int j=0; j<3; j++)
		{
			sum += ptr[i].mark[j];
		}
		total[i] = sum;
			
		phy += ptr[i].mark[0];
		chem += ptr[i].mark[1];
		mat += ptr[i].mark[2];
	}

	// Printing Student details
	for(int i=0; i<2; i++)
	{
		printf("e%d :: stdID | name | phone | email | Physics | Chemistry | Maths | Total\n", i+1);
		printf("e%d :: stdID : %d | name : %s | phone : %s | email : %s | ", i+1, ptr[i].stdID, ptr[i].name, ptr[i].phone, ptr[i].email);
		for(int j=0; j<3; j++)
		{
			printf("%d | ", ptr[i].mark[j]);
		}
		printf("Total :%d | Physics : %d | Chemistry : %d | Maths : %d |", total[i], phy, chem, mat);
		printf("\n");
	}

	return 0;
}
