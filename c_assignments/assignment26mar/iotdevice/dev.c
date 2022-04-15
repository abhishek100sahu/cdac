#include"device.h"
#include<stdio.h>

/*
struct Device
{
	int deviceId;
	char deviceName[100];
	char deviceType[10];
	int voltage;
} device;

struct Home
{
	int homeId;
	char homeOwner[100];
	char address[100];
	device dev;
} home;
*/

// Menu
int menu()
{
	int button = 0;	
	printf("\nPress [1] : Add Device\n");
	printf("Press [2] : Display Device\n");
	printf("Press [3] : Search Device\n");
	printf("Press [4] : Change Device\n");
	printf("Press [5] : Exit\n");
	scanf("%d", &button);

	return button;
}

// taking user input
void input(home* arr, int* n, int* ndev)
{	// homeId
	printf("Enter homeId : ");
	scanf("%d", &arr[*n].homeId);
	// homeOwner
	printf("Enter homeOwner : ");
	scanf("%s", arr[*n].homeOwner);
	// address
	printf("Enter address : ");
	scanf("%s", arr[*n].address);
	
	// device
	for(int i=0; i<(*ndev); i++);
	{	
		printf("Enter deviceId : ");
		scanf("%d", &arr[*n].dev.deviceId);
		printf("Enter deviceName : ");
		scanf("%s", arr[*n].dev.deviceName);
		printf("Enter deviceType : ");
		scanf("%s", arr[*n].dev.deviceType);
		printf("Enter voltage : ");
		scanf("%d", &arr[*n].dev.voltage);
	}

	++(*n);
}

// Providing device details
void display(home* arr, int* n, int* ndev)
{
	for(int i=0; i<*n; i++)
	{
		printf("homeId : %d | ",arr[i].homeId);
		printf("homeOwner : %s | ",arr[i].homeOwner);
		printf("address : %s | ",arr[i].address);		
		printf("deviceId : %d | ",arr[i].dev.deviceId);
		printf("deviceName : %s | ",arr[i].dev.deviceName);
		printf("deviceType : %s | ",arr[i].dev.deviceType);
		printf("voltage : %d | ",arr[i].dev.voltage);
		printf("\n");
		
	}
}

// Search Device
void search(home* arr, int* n, int* ndev)
{	
	int id;
	printf("Enter the deviceId : ");
	scanf("%d", &id);
	
	for(int i=0; i<*n; i++)
	{
		if(arr[i].dev.deviceId == id)
		{
			printf("homeId : %d | ",arr[i].homeId);
			printf("homeOwner : %s | ",arr[i].homeOwner);
			printf("address : %s | ",arr[i].address);
			printf("deviceId : %d | ",arr[i].dev.deviceId);
			printf("deviceName : %s | ",arr[i].dev.deviceName);
			printf("deviceType : %s | ",arr[i].dev.deviceType);
			printf("voltage : %d | ",arr[i].dev.voltage);
			printf("\n");
		
		}
	}

	printf("Enter the homeId : ");
	scanf("%d", &id);
	for(int i=0; i<*n; i++)
	{
		if(arr[i].homeId == id)
		{
			printf("homeId : %d | ",arr[i].homeId);
			printf("homeOwner : %s | ",arr[i].homeOwner);
			printf("address : %s | ",arr[i].address);
			printf("deviceId : %d | ",arr[i].dev.deviceId);
			printf("deviceName : %s | ",arr[i].dev.deviceName);
			printf("deviceType : %s | ",arr[i].dev.deviceType);
			printf("voltage : %d | ",arr[i].dev.voltage);
			printf("\n");
		}
	}
}

// Updating employee name
void change(home* arr, int* n, int* ndev)
{
	int id;
	printf("Enter the deviceId : ");
	scanf("%d", &id);

	for(int i=0; i<*n; i++)
	{
		
		if(arr[i].dev.deviceId == id)
		{
			printf("Updated name : ");
			scanf("%s", arr[i].dev.deviceName);
			printf("Update Succesfully!\n");						
		}
		
	}
}

