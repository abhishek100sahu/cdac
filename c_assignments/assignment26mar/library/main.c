#include"libr.h"

int main()
{
	lib l[10];
	lib* ptr = l;
	int button = 0, n = 0;

	do
	{
		button = menu();
		
		if(button == 1)
		{
			input(ptr,&n);
		}
		else if(button == 2)
		{
			display(ptr, &n);
		}
		else if(button == 3)
		{
			search(ptr, &n);	
		}
		else if(button == 4)
		{
			break;
		}
		else
		{
			printf("Invalid input");
		}
	}
	while(1);

	

	return 0;
}
