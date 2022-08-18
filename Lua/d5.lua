s=... -- input
-- Part 1
c=0 for x in s:gmatch"%S+"do c=c+(x:find((".-[aeiou]"):rep(3))and x:find"(.)%1"and not(x:find"ab"or x:find"cd"or x:find"pq"or x:find"xy")and 1 or 0)end print(c)
-- Part 2
c=0 for x in s:gmatch"%S+"do c=c+(x:find"(..).-%1"and x:find"(.).%1"and 1 or 0)end print(c)
-- Both parts
c=0 d=0 for x in s:gmatch"%S+"do c=c+(x:find((".-[aeiou]"):rep(3))and x:find"(.)%1"and not(x:find"ab"or x:find"cd"or x:find"pq"or x:find"xy")and 1 or 0)d=d+(x:find"(..).-%1"and x:find"(.).%1"and 1 or 0)end print(c,d)
