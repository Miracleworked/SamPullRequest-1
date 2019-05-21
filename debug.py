def lone_sum(a, b, c):
    if a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    elif a == b and a == c and b == c:
        return 0
    else:
        return a+b+c

#this the fixed code
    #There are 3 integer values a, b, and c and 
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
print(lone_sum(3,5,7)
