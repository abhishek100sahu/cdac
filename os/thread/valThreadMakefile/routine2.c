#include<unistd.h>
int val;

void *routine2(void *msg){
    sleep(10);
    val += 5;
    printf("val : %d\n",val);
}