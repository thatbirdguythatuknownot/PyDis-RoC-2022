#include <stdio.h>
int main(){
    const char*s=""; /* input */
    /* Part 1 */ {
    const char*y=s;
    int x=0;
    for (char c=*y;c;c=*++y)x+=1|-(c-'(');
    printf("%d\n",x);
    } /* Part 2 */ {
    int x=1,i=0;
    for (;s[i];++i) {
        x+=1|-(s[i]-'(');
        if(!x){
            printf("%d\n",i);
            break;
        }
    }
    } /* Both parts */ {
    int y=1,x=1,i=0;
    for (;s[i];++i) {
        x+=1|-(s[i]-'(');
        if(y&!x){
            y=0;
            printf("%d\n",i);
        };
    }
    printf("%d\n",x-1);
}}
