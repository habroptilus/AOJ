#include "stdio.h"
#define N 50

int solve(int m,int digit){
    int i,sum;
    sum=0;
    if (digit==1){
        for (i = 0; i < 10; i++) {
            if(i==m)return 1;
        }
        return 0;
    }
    for (i = 0; i < 10; i++) {
    sum=sum+solve(m-i,digit-1);
    }
    return sum;
}

int main(int argc, char const *argv[]) {
    int n[N],i,j;
    i=0;
    while(scanf("%d",&n[i])!=EOF)i++;
    for (j = 0; j < i; j++) {
        printf("%d\n",solve(n[j],4));
    }
    return 0;
}
