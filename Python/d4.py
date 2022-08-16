s=... # input
# Part 1
import hashlib;x=0;print(next(x for _ in iter(int,1)if hashlib.md5(f"{s}{(x:=x+1)}".encode()).hexdigest().startswith('0'*5)))
# Part 2
import hashlib;x=0;print(next(x for _ in iter(int,1)if hashlib.md5(f"{s}{(x:=x+1)}".encode()).hexdigest().startswith('0'*6)))
# Both parts
import hashlib;f=lambda n,x=0:print(next(x for _ in iter(int,1)if hashlib.md5(f"{s}{(x:=x+1)}".encode()).hexdigest().startswith('0'*n)));f(5);f(6)
