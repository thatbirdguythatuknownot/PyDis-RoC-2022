s=... # input
# Part 1
print(len(s)-eval(f'len({s})')-299)
# Part 2
print(600+sum(map(s.count,'"\\')))
# Both parts
print(len(s)-eval(f'len({s})')-299,600+sum(map(s.count,'"\\')))
