s=... # input
# Part 1
import hashlib;x=0;print(next(x for _ in iter(int,1)if'0'*5==hashlib.md5(f"{s}{(x:=x+1)}".encode()).hexdigest()))
# Part 2
import hashlib;x=0;print(next(x for _ in iter(int,1)if'0'*6==hashlib.md5(f"{s}{(x:=x+1)}".encode()).hexdigest()))
# Both parts
import hashlib;f=lambda n,x=0:print(next(x for _ in iter(int,1)if'0'*n==hashlib.md5(f"{s}{(x:=x+1)}".encode()).hexdigest()));f(5);f(6)
