#include"emp.h"

int main()
{
	employee emp[100];
	int button = 0, n=0;
	employee* ptr = emp;

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
			change(ptr, &n);
		}
		else if(button == 5)
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
