#include<stdio.h>

int main(int argc, char const *argv[]) {
    int x,y,r,W,H;
    scanf("%d %d %d %d %d",&W,&H,&x,&y,&r);
if((x-r>=0)&&(x+r<=W)&&(y-r>=0)&&(y+r<=H))printf("Yes\n");
else printf("No\n");
return 0;
}
