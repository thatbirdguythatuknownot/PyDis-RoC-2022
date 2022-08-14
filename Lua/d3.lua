s=... -- input
-- Part 1
a,b,c=0,0,1 l={[0]={[0]=1}}for x in s:gmatch'.'do a=a+(x:find'[<>]'or 0)*(1|-(x:find'>'or 0))b=b+(x:find'[v^]'or 0)*(1|-(x:find'v'or 0))if not l[a]then l[a]={}end if not l[a][b]then c=c+1 end l[a][b]=1 end print(c)
-- Part 2
l={[0]={[0]=1}}c,i,a=1,0,{[-1]={0,0},[0]={0,0}}for x in s:gmatch'.'do t=a[i]m=t[1]+(x:find'[<>]'or 0)*(1|-(x:find'>'or 0))t[1]=m n=t[2]+(x:find'[v^]'or 0)*(1|-(x:find'v'or 0))t[2]=n if not l[m]then l[m]={}end if not l[m][n]then c=c+1 end l[m][n]=1 i=~i end print(c)
