#include<stdio.h>

typedef struct Library
{
	int bookId;
	char bookName[100];
	char ISBN[10];
	char author[100];
} lib;

// Menu
int menu()
{
	int button = 0;	
	printf("\nPress [1] : Add Book\n");
	printf("Press [2] : Display Books\n");
	printf("Press [3] : Search Book\n");
	printf("Press [4] : Exit\n");
	scanf("%d", &button);

	return button;
}

// taking user input
void input(lib* arr, int* n)
{	// bookId
	printf("Enter bookId : ");
	scanf("%d", &arr[*n].bookId);
	// bookName
	printf("Enter bookName : ");
	scanf("%s", arr[*n].bookName);
	// ISBN
	printf("Enter ISBN : ");
	scanf("%s", arr[*n].ISBN);
	// Author	
	printf("Enter Author : ");
	scanf("%s", arr[*n].author);

	++(*n);
}

// Providing Book details
void display(lib* arr, int* n)
{
	for(int i=0; i<*n; i++)
	{
		printf("bookId : %d | ",arr[i].bookId);
		printf("bookName : %s | ",arr[i].bookName);
		printf("ISBN : %s | ",arr[i].ISBN);
		printf("author : %s | ",arr[i].author);
		printf("\n");
	}
}
// Search book
void search(lib* arr, int* n)
{	
	int id;
	printf("Enter the bookId : ");
	scanf("%d", &id);
	
	for(int i=0; i<*n; i++)
	{
		if(arr[i].bookId == id)
		{
			printf("bookId : %d | ",arr[i].bookId);
			printf("bookName : %s | ",arr[i].bookName);
			printf("ISBN : %s | ",arr[i].ISBN);
			printf("author : %s | ",arr[i].author);
			printf("\n");
		}
	}
}

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
