#include<stdio.h>

typedef struct Date
{
	int dd;
	int mm;
	int yyyy;
} date;

typedef struct Student
{
	char name[100];
	int pnr;
	date dob;
} std;

int main()
{
	FILE* fp = fopen("4.txt", "a+");
	std s1;
	
	printf("name : ");
	scanf("%s", s1.name);
	fprintf(fp, "name : %s | ", s1.name);

	printf("pnr : ");
	scanf("%d", &s1.pnr);
	fprintf(fp, "pnr : %d | ", s1.pnr);

	printf("Date of Birth : \n");
	
	printf("date : ");
	scanf("%d", &s1.dob.dd);
	fprintf(fp, "%d.", s1.dob.dd);
	
	printf("month : ");
	scanf("%d", &s1.dob.mm);
	fprintf(fp, "%d.", s1.dob.mm);
	
	printf("year : ");
	scanf("%d", &s1.dob.yyyy);
	fprintf(fp, "%d\n", s1.dob.yyyy);

	fseek(fp, 0, SEEK_END);	

	return 0;
}
