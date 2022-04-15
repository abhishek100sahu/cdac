typedef struct Date
{
	int dd;
	int mm;
	int yyyy;
} date;

typedef struct Address
{
	int flatNo;
	char city[100];
	char state[100];
} addr;

typedef struct Employee
{
	char name[100];
	int empId;
	date dob;
	addr ad;
} employee;
	
