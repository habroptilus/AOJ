#include<stdio.h>
#include<string.h>
int main() {

    char str[21],rev[21];
    int i,j;
    memset(str,'\0', 21);
    scanf("%s",str);
    j=0;
    for (i = 0; i < 21; i++) {
        if (str[20-i]!='\0'){
             rev[j]=str[20-i];
             j++;
         }
    }

    for (i = 0; i < 21-j; i++) {
    rev[i+j]='\0';
    }
    //printf("%s\n",str);
    printf("%s\n",rev);


    return 0;
}
