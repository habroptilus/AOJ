
#include<stdio.h>
#include<stdlib.h>

int max(int *a,int n){
    int i;
    int max=-1000000;
    int max_i=-1;
    for (i = 0; i < n; i++) {
        if (max<a[i]) {
            max=a[i];
            max_i=i;
        }
    }
    return max_i;
}


int main(){

int N,i,j,sum;
int **a;

scanf("%d",&N);

a=malloc(N*sizeof(int*));
for (i = 0; i < N; i++) {
    a[i]=malloc(3*sizeof(int));
}
for (i = 0; i < N; i++) {
        scanf("%d %d %d",&a[i][0],&a[i][1],&a[i][2]);
    }
for (i = 0; i < N; i++) {
    sum=0;
    for (j = 0; j < 3; j++) {
        if (j!=max(a[i],3)) {
            sum=sum+a[i][j]*a[i][j];
        }
    }
    if ((a[i][max(a[i],3)])*(a[i][max(a[i],3)])==sum) printf("YES\n");
    else printf("NO\n");
}

return 0;
}
