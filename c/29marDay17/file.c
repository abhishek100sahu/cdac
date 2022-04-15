#include<stdio.h>

int main()
{
	FILE *fd = fopen("data.txt", "r+");
	char data[100];

	// read
	fread(data, 10, 1, fd);
	printf("Data from file : %s\n", data);

	// write
	char str[100];
	printf("Enter some data to write into the file : \n");
	scanf("%s", str);

	int res = fwrite(str, 10, 1, fd);

	printf("return value of ret : %d\n", res);

	fclose(fd);

	return 0;
}

