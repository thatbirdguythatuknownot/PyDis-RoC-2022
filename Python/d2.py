s=... # input
# Part 1
c=0;p=str.split
for x in p(s):l,w,h=map(int,p(x,'x'));c+=2*sum(y:=(l*w,w*h,h*l))+min(y)
print(c)
# Part 2
c=0;p=str.split
for x in p(s):l,w,h=map(int,p(x,'x'));c+=2*sum(sorted([l,w,h])[:2])+l*w*h
print(c)
# Both parts
c=d=0;p=str.split
for x in p(s):l,w,h=map(int,p(x,'x'));c+=2*sum(y:=(l*w,w*h,h*l))+min(y);d+=2*sum(sorted([l,w,h])[:2])+l*w*h
print(c,d,sep='\n')
