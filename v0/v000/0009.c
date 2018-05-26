#include "stdio.h"
#include "math.h"
#define N 30

int Eratosthenes_sieve(int n){
    int count=0;
    int a[n+1],i;
    int j=2;
    for (i = 0; i < n+1; i++) {
        a[i]=1;
    }
    for (i = 2; i < (int)sqrt((double)n)+1; i++) {
        if (a[i]==1) {
            while (i*j<=n) {
                a[i*j]=0;
                j++;
            }
            j=2;
        }
    }
    for (i = 2; i < n+1; i++) {
        if (a[i]==1)count++;
    }
    return count;
}

int main() {
    int n[N],i,j;
    i=0;
    while(scanf("%d",&n[i])!=EOF)i++;
    for (j = 0; j < i; j++) {
        printf("%d\n",Eratosthenes_sieve(n[j]));
    }
    return 0;
}
