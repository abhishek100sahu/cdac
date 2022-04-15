int str_length(char* name)
{
	int len = 0;
	int i = 0;
	while(name[i] != '\0')
	{
		len++;
		i++;
	}
	
	return len;
}

// Comparision of 2 string
int str_cmp(char* name, char* other)
{
	int i = 0;
	while(name[i] != '\0')
	{
		if(name[i] != other[i])
		{
			break;
		}
		i++;	
	}

	if(name[i] == '\0' && other[i] == '\0')
		return 1;// true
	return 0;// false
}

// concatinating two arrays
int str_concat(char* name, char* other, char* concatination)
{
	int j=0;
	for(int i=0; name[i] != '\0'; ++i){
		concatination[j] = name[i];
		j++;
	}
	for(int i=0; other[i] != '\0'; ++i){
		concatination[j] = other[i];
		j++;
	}
	concatination[j] = '\0';
}
		
// Reversing in memory
void rev(char* con, int l)
{
	int a = 0, b = l-1;
	while(a < b) 
	{
		char temp = *(con+a);
		*(con+a) = *(con+b);
		*(con+b) = temp;
		a++;
		b--;
	}
}

// Finding 1st occurance
int first_occurance(char* c, char ch)
{
	int i = 0, pos = -1;
	while(c[i] != '\0')
	{
		if(c[i] == ch)
		{
			pos = i;
			break;
		}
		i++;
	}
	
	return pos;
}

// Finding Last Occurance
int last_occurance(char* c, char ch)
{
	int i = 0, pos = -1;
	while(c[i] != '\0')
	{
		if(c[i] == ch)
		{
			pos = i;
		}
		i++;
	}
	
	return pos;
}

// Count occurance
int count_occurance(char* c, char ch)
{
	int i = 0, count = 0;
	while(c[i] != '\0')
	{
		if(c[i] == ch)
		{
			count++;
		}
		i++;
	}
	return count;
}

// Sub string
int substring(char* c, char* sub)
{
	int i = 0, j = 0;
	while(c[i] != '\0')
	{
		if(c[i] == sub[j])
		{		
			while(c[i] != '\0' && sub[j] != '\0')
			{
				if(c[i] != sub[j])
					break;
				j++;
				i++;
			}
		}
		
		if(sub[j] == '\0')
			return 1;// true
		i++;
	}

	return 0;// false
}
