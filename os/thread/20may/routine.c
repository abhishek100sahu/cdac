int testValue=0;

void *routine(void *msg){
    for(int i=0;i<10000;i++){
        testValue++;
        printf("testValue : %d\n",testValue);
    }
}