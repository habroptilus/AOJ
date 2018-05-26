#include<stdio.h>
#include<math.h>
#define N 15
int main() {
    double X,Y,a[N][6],x[N],y[N],det[N];
    int i=0;
    int j;
    while (scanf("%lf",&a[i][0])!=EOF) {
        for (j = 1; j < 6; j++) {
            scanf("%lf",&a[i][j]);
        }
        i++;
    }

    for (j = 0; j < i; j++) {
        det[j]=a[j][0]*a[j][4]-a[j][1]*a[j][3];
        x[j]=a[j][2]*a[j][4]-a[j][1]*a[j][5];
        y[j]=a[j][0]*a[j][5]-a[j][2]*a[j][3];
    }
    for (j = 0; j < i; j++) {
        X=floor(1000*x[j]/det[j]+0.5);
        Y=floor(1000*y[j]/det[j]+0.5);
        printf("%.3f %.3f\n",X/1000.0,Y/1000.0);
    }
    return 0;
}
