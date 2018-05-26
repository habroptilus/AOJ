#include<stdio.h>

void InsertSort(int *a,int n){
    int i,j,v;

    for (i = 1; i < n; i++) {
        v=a[i];
        j=i-1;
        while (j!=-1&&a[j]>v) {
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=v;

    }

}


int main(int argc, char const *argv[]) {
    int a[3],i;
    for (i = 0; i < 3; i++) {
    scanf("%d",&a[i]);
    }
    InsertSort(a,3);
    for (i = 0; i < 2; i++) {
        printf("%d ",a[i]);
    }
    printf("%d\n",a[2]);
    return 0;
}
