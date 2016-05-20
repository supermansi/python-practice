#from __builtins__ import hash

n = int(input())
t = tuple(int(i) for i in input().split())
print(hash(t))    
