# Part 1
s = ...
print((_:=s.count)('(')-_(')'))
# Part 2
print([i-2*s[:i].count(')')for i in range(len(s))].index(-1))
# Both parts
print(*[(f:=1)+[f:=f+(1|-(x==')'))for x in input()].index(0),f-1][::-1]) # Most of the logic taken from <@!397120199897120769>
