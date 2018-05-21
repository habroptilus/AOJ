#include<stdio.h>
#define N 50
int Euclid(int a,int b){

if (a%b==0) return b;

return Euclid(b,a%b);
}


int main() {

    int a[N],b[N],temp,i,j;
    double x,y;
    i=0;
    while (scanf("%d",&a[i])!=EOF) {
    scanf("%d",&b[i]);
    i++;
    }
    for (j = 0; j < i; j++) {
        if (b[j]>a[j]) {
            temp=a[j];
            a[j]=b[j];
            b[j]=temp;
        }
    }
    for (j = 0; j < i; j++) {
    y=(double)Euclid(a[j],b[j]);
    x=(double)a[j]*((double)b[j]/y);
    printf("%d %d\n",(int)y,(int)x);
    }


    return 0;
}
