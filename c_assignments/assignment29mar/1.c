#include<stdio.h>

int main()
{
	FILE* fd = fopen("data.txt", "r+");
	char a[10] = "abhishek";

	fputs(a, fd);
	fclose(fd);	

	return 0;
}
