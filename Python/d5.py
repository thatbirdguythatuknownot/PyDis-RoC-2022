s=... # input
# Part 1
import re;print(sum(all(map(re.search,('(.*[aeiou]){3}',r'(.)\1','^((?!ab|cd|pq|xy).)*$'),[u]*3))for u in s.split()))
# Part 2
import re;print(sum(all(map(re.search,(r'(..).*\1',r'(.).\1'),[u,u]))for u in s.split()))
# Both parts
import re;f=lambda*a:print(sum(all(map(re.search,a,[u]*len(a)))for u in s.split()));f('(.*[aeiou]){3}',r'(.)\1','^((?!ab|cd|pq|xy).)*$'),f(r'(..).*\1',r'(.).\1')
