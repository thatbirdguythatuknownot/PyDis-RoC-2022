s=... -- input
-- Part 1
t=tonumber c=0 p=("").gmatch for x in p(s,"[^\n]+")do f=p(x,"%d+")l,w,h=t(f()),t(f()),t(f())y={l*w,w*h,h*l}table.sort(y)c=c+3*y[1]+2*(y[2]+y[3])end print(c)
-- Part 2
t=tonumber c=0 p=("").gmatch for x in p(s,"[^\n]+")do f=p(x,"%d+")l,w,h=t(f()),t(f()),t(f())y={l,w,h}table.sort(y)c=c+2*(y[1]+y[2])+l*w*h end print(c)
-- Both parts
t=tonumber c=0 d=0 b=table.sort p=("").gmatch for x in p(s,"[^\n]+")do f=p(x,"%d+")l,w,h=t(f()),t(f()),t(f())y={l*w,w*h,h*l}b(y)c=c+3*y[1]+2*(y[2]+y[3])y={l,w,h}b(y)d=d+2*(y[1]+y[2])+l*w*h end p=print p(c)p(d)
