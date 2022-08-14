s=... # input
# Part 1
l=[[a,b]]={(0,0)}
for x in s:a+=(x in'<>')*(1|-(x=='<'));b+=(x in'^v')*(1|-(x=='v'));l.add((a,b))
print(len(l))
# Part 2
l={(0,0)};a=[[0,0],[0,0]];i=0
for x in s:(o:=a[i])[0]+=(x in'<>')*(1|-(x=='<'));o[1]+=(x in'^v')*(1|-(x=='v'));l.add((*o,));i=~i
print(len(l))
# Both parts
l=[[m,n]]=(k:={(0,0)}).copy();a=[[0,0],[0,0]];i=0
for x in s:(o:=a[i])[0]+=(c:=(x in'<>')*(1|-(x=='<')));m+=c;o[1]+=(c:=(x in'^v')*(1|-(x=='v')));n+=c;l.add((*o,));i=~i;k.add((m,n))
print(len(k),len(l),sep='\n')
