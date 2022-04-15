#include"iotdevice.h"

int main()
{
	home iot[100];
	int button = 0, n=0, ndev=5;
	home* ptr = iot;

	do
	{
		button = menu();
		
		if(button == 1)
		{
			input(ptr, &n, &ndev);
		}
		else if(button == 2)
		{
			display(ptr, &n, &ndev);
		}
		else if(button == 3)
		{
			search(ptr, &n, &ndev);	
		}
		else if(button == 4)
		{
			change(ptr, &n, &ndev);
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
