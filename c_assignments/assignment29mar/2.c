/*
2.Write a menu driven program to read data from  file and perform airthmatic calculation.
*/
#include<stdio.h>

void menu()
{
	printf("Press[1] : add\n");
	printf("Press[2] : sub\n");
	printf("Press[3] : mul\n");
	printf("Press[4] : div\n");
	printf("Press[5] : Exit\n");
}

int add(FILE* fp)
{
	int a, b;
	fscanf(fp, "%d%d", &a, &b);
	
	return a + b;
}

int sub(FILE* fp)
{
	int a, b;
	fscanf(fp, "%d%d", &a, &b);
	
	return a - b;
}

int mul(FILE* fp)
{
	int a, b;
	fscanf(fp, "%d%d", &a, &b);
	
	return a * b;
}

int div(FILE* fp)
{
	int a, b;
	fscanf(fp, "%d%d", &a, &b);
	
	return a / b;
}

int main()
{
	FILE* fp = fopen("/home/rajesh/220106871_AbhishekSahu/assignments/assignment29mar/data1.txt", "r+");
	int ch;
	int res = 0;
	
	while(1)
	{
		menu();
		printf("Enter choice : \n");
		scanf("%d", &ch);
		
		if(ch == 5)
			break;

		switch(ch)
		{
			case 1:
			{
				res = add(fp);
				fprintf(fp, "\nSum : %d\n", res);				
				rewind(fp);
				break;
			}	
			case 2:
			{
				res = sub(fp);
				printf("Sub : %d\n", res);
				rewind(fp);
				break;
			}
			case 3:
			{
				res = mul(fp);
				printf("mul : %d\n", res);
				rewind(fp);				
				break;
			}
			case 4:
			{
				res = div(fp);
				printf("Div : %d\n", res);
				rewind(fp);
				break;
			}
			default:
				printf("Invalid");
		}
	}	

	return 0;
}
