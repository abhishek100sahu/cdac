#include<stdio.h>
#include<string.h>

int main()
{
	FILE* fp = fopen("4.txt", "r");
	char x[100];
	
	fseek(fp, 7,SEEK_SET);
	fread(x, 8, 1, fp);
	printf("%s", x);
	memset(x, 0, 100);

	fseek(fp, 24,SEEK_SET);
	fread(x, 3, 1, fp);
	printf(" %s", x);
	memset(x, 0, 100);

	fseek(fp, 30,SEEK_SET);
	fread(x, 9, 1, fp);
	printf(" %s\n", x);
	memset(x, 0, 100);

	fseek(fp, 8,SEEK_CUR);
	fread(x, 8, 1, fp);
	printf("%s", x);
	memset(x, 0, 100);

	fseek(fp, 24,SEEK_SET);
	fread(x, 3, 1, fp);
	printf(" %s", x);
	memset(x, 0, 100);

	fseek(fp, 30,SEEK_SET);
	fread(x, 9, 1, fp);
	printf(" %s\n", x);
	memset(x, 0, 100);

	fseek(fp, 8,SEEK_CUR);
	fread(x, 8, 1, fp);
	printf("%s", x);
	memset(x, 0, 100);

	fseek(fp, 24,SEEK_SET);
	fread(x, 3, 1, fp);
	printf(" %s", x);
	memset(x, 0, 100);

	fseek(fp, 30,SEEK_SET);
	fread(x, 9, 1, fp);
	printf(" %s\n", x);
	memset(x, 0, 100);
	
	return 0;
}
