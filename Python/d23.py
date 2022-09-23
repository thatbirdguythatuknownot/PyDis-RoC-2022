s=... # input
# Part 1
d={'a':0,'b':0};n=s.split('\n');l=0
while l<len(n):
 x=n[l];g=x[2];r=x[4]
 if f:={'o':1 .__eq__,'e':lambda y:0==y&1}.get(g):l+=(int(x[x.find(',')+1:])-1)*f(d[r])
 elif f:={'f':lambda y:y//2,'l':3 .__mul__,'c':1 .__add__}.get(g):d[r]=f(d[r])
 else:l+=int(x[4:])-1
 l+=1
# Part 2
d={'a':1,'b':0};n=s.split('\n');l=0
while l<len(n):
 x=n[l];g=x[2];r=x[4]
 if f:={'o':1 .__eq__,'e':lambda y:0==y&1}.get(g):l+=(int(x[x.find(',')+1:])-1)*f(d[r])
 elif f:={'f':lambda y:y//2,'l':3 .__mul__,'c':1 .__add__}.get(g):d[r]=f(d[r])
 else:l+=int(x[4:])-1
 l+=1
# Both parts
d={'a':0,'b':0};n=s.split('\n');exec(a:='''l=0
while l<len(n):
 x=n[l];g=x[2];r=x[4]
 if f:={'o':1 .__eq__,'e':lambda y:0==y&1}.get(g):l+=(int(x[x.find(',')+1:])-1)*f(d[r])
 elif f:={'f':lambda y:y//2,'l':3 .__mul__,'c':1 .__add__}.get(g):d[r]=f(d[r])
 else:l+=int(x[4:])-1
 l+=1
print(d['b'])''');d={'a':1,'b':0};exec(a)
