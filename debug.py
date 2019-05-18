def lone_sum(a, b, c):
if a == b and a == c and b == c:
   return 0
elif a >= b:
   return c
elif b == c:
   return a
elif a == c:
   return c
else:
   return a+b+c
print(lone_sum(1,1,2))
