#include<unistd.h>
int val;

void *routine1(void *msg){
    val += 2;
    printf("val : %d\n",val);
    sleep(10);
}