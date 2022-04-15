typedef struct Device
{
	int deviceId;
	char deviceName[100];
	char deviceType[10];
	int voltage;
} device;

typedef struct Home
{
	int homeId;
	char homeOwner[100];
	char address[100];
	device dev;
} home;
