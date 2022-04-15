#include<stdio.h>

int srt_length(char* str)
{
	int len;
	int i = 0;
	while(str[i] != '\0')
	{
		len++;
		i++;
	}
	
	return len;
}

int str_cmp(char* str1, char* str2)
{
	int i = 0;
	while(str1[i] != '\0')
	{
		if(str1[i] != str2[i])
		{
			break;
		}
		i++;	
	}

	if(str1[i] == '\0' && str2[i] == '\0')
		return 1;// true
	return 0;// false
}
		

int main()
{
	char name[100];
	char other[100];
	printf("1st name :");
	scanf("%s", &name);
	printf("2nd name :");
	scanf("%s", &other);

	int res = str_cmp(name, other);
	int length = str_length(name);


	if(res == 0)	
		printf("false : %d\n", res);
	else
		printf("true : %d\n", res);

	return 0;
}
