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
    #There are 3 integer values a, b, and c. Two of the values is equal to the other
def lone_sum(a, b, c):  # definition of lone_sum
    if a == b and a == c and b == c:  #if all values equal each other return 0
        return 0 
    elif a >= b:     # if a is greater than/equal to b, return value of c
        return c 
    elif b == c:     #if b is equal to c, return value of a
        return a
    elif a == c:     #elseif a equal c, return c
     return c
    else:            #else if all values fail, return the sum of a,b and c
        return a+b+c
print(lone_sum(3,5,7)  #enter values to check code, print sum is 15
