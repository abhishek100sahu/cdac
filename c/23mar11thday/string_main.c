#include"string_opr.h"
#include<stdio.h>

int main()
{
	char name[100];
	char other[100];
	char concatination[100];
	char substr[50];
	int length, l;
	char ch;

	// Taking input from user	
	printf("1st name :");
	scanf("%s", name);
	printf("2nd name :");
	scanf("%s", other);

	// Length of name
	length = str_length(name);
	printf("Length : %d\n", length);

	// Comparing name & other
	int res = str_cmp(name, other);
	if(res == 0)	
		printf("StringMatch : false : %d\n", res);
	else
		printf("StringMatch : true : %d\n", res);

	// Adding 2 string
	str_concat(name, other, concatination);
	printf("Concatination : %s\n", concatination);

	// Reversing array
	l = str_length(concatination);
	rev(concatination, l);
	printf("Reverse : %s\n", concatination);
	rev(concatination, l);

	// First occurance
	printf("Character for 1st occurance : ");
	scanf("%c", &ch);
	scanf("%c", &ch);
	int occ = first_occurance(concatination, ch);
	printf("Character %c's 1st occurance @ [%d] index \n", ch, occ);

	// Last occurance
	printf("Character for last occurance : ");
	scanf("%c", &ch);
	scanf("%c", &ch);
	int locc = last_occurance(concatination, ch);
	printf("Character %c's last occurance @ [%d] index \n", ch, locc);

	// No. of occurance
	printf("Character for finding no. of occurance : ");
	scanf("%c", &ch);
	scanf("%c", &ch);
	int no = count_occurance(concatination, ch);
	printf("Character %c's no. of occurance : %d\n", ch, no);

	// Sub string
	printf("Substring : ");
	scanf("%s", substr);
	int ss = substring(concatination, substr); 
	if(ss == 0)	
		printf("SubstringMatch : false : %d\n", ss);
	else
		printf("SubstringMatch : true : %d\n", ss);	

	return 0;
}
