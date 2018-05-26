#include<stdio.h>


int main() {
    int a[200],b[200],c;
    int i,j,digit;
    i=0;
    while (scanf("%d",&a[i])!=EOF) {
        scanf("%d",&b[i]);
        i++;
    }
    for (j = 0; j < i; j++) {
        c=a[j]+b[j];
        digit=1;
        while((c=c/10)!=0)digit++;
    printf("%d\n",digit);
    }
    return 0;
}
