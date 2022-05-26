#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include<unistd.h>

int testValue=1;
pthread_mutex_t mutex;

void *routine(void *msg){
    for(int i=1;i<1000000;i++){
        pthread_mutex_lock(&mutex);
        testValue++;
        pthread_mutex_unlock(&mutex);
        //printf("testValue : %d\n",testValue);
    }
}

int main(int argc, char* argv[]){

    pthread_t t1;
    pthread_t t2;

    pthread_create(&t1, NULL, routine,NULL);
    //pthread_join(t1,NULL);
    

    pthread_create(&t2,NULL,routine,NULL);
    pthread_join(t1,NULL);
    pthread_join(t2,NULL);
   

    printf("testValue : %d\n",testValue);
    return 0;
}