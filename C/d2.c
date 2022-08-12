#include <stdio.h>
int main(){
    const char*s=""; /* input */
    /* Part 1 */ {
    const char*f=s;
    int l,w,h,x,y,z,n,c=0;
    while(sscanf(f,"%dx%dx%d\n%n",&l,&w,&h,&n)>2){
        f+=n;
        x=l*w;
        y=w*h;
        z=h*l;
        c+=2*(x+y+z)+(x<y&&x<z?x:y<z?y:z);
    }
    printf("%d\n",c);
    } /* Part 2 */ {
    const char*f=s;
    int l,w,h,n,c=0;
    while(sscanf(f,"%dx%dx%d\n%n",&l,&w,&h,&n)>2){
        f+=n;
        c+=2*(l<w?(w<h?l+w:l+h):l<h?w+l:w+h)+l*w*h;
    }
    printf("%d\n",c);
    } /* Both parts */ {
    const char *f=s;
    int l,w,h,x,y,z,n,c=0,d=0;
    while(sscanf(f,"%dx%dx%d\n%n",&l,&w,&h,&n)>2){
        f+=n;
        x=l*w;
        y=w*h;
        z=h*l;
        c+=2*(x+y+z)+(x<y&&x<z?x:y<z?y:z);
        d+=2*(l<w?(w<h?l+w:l+h):l<h?w+l:w+h)+l*w*h;
    }
    printf("%d\n%d\n",c,d);
}}
