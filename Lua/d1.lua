s = ... -- input
-- Part 1
print(({s:gsub('(','')})[2]-({s:gsub(')','')})[2])
-- Part 2
x=0
i=1
repeat
    x=x+(-1)^(s:sub(i,i)==')'and 1 or 0)
    i=i+1
until x<0
print(i)
-- Both parts
x=1
i=1
f=s:gmatch"."
for c in f do
    x=x+(1|-(c==')'and 1 or 0))
    if i then
        if x == 0 then
            print(i)
            i=false
        else i=i+1 end
    end
end
print(x-1)
