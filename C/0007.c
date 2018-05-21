#include "stdio.h"
#include "math.h"
int main() {

    int i,n;
    scanf("%d",&n);
    if (n==0) {
        printf("%d\n",100000);
        return 0;
    }
    double result=100000;
    for (i = 0; i < n; i++) {
        result=result*1.05;
        result=1000*ceil(result/1000);
    }
    printf("%d\n",(int)result);
    return 0;
}
