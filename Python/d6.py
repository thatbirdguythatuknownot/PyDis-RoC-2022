s=... # input
# Part 1
import re;from itertools import*;a={*()}
for u in s.split('\n'):g={*product(*[range(int(x[0]),int(x[1])+1)for x in zip(*re.findall("(\d+),(\d+)",u))])};a=a^g if'l'in u else a-g if'f'in u else a|g
print(len(a))
# Part 2
import re,numpy;from itertools import*;a=numpy.zeros([1000]*2)
for u in s.split('\n'):
 for m in product(*[range(int(x[0]),int(x[1])+1)for x in zip(*re.findall("(\d+),(\d+)",u))]):a[m]+=2 if'l'in u else 0!=a[m]and-1 if'f'in u else 1
print(a.sum())
# Both parts
import re,numpy;from itertools import*;a,b={*()},numpy.zeros([1000]*2)
for u in s.split('\n'):
 g={*()}
 for m in product(*[range(int(x[0]),int(x[1])+1)for x in zip(*re.findall("(\d+),(\d+)",u))]):g.add(m);b[m]+=2 if'l'in u else 0!=b[m]and-1 if'f'in u else 1
 a=a^g if'l'in u else a-g if'f'in u else a|g
print(len(a),b.sum())
