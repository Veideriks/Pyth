# 26

x = a = int(input())
b = int(input())
def step (a,b):
    if b>1:
        return step (a*x,b-1)
    return a

print (step (a,b))

# 28

a = int(input())
b = int(input())

def sum (a,b):
    if b!=0:
        return sum (a+1,b-1)
    return a

print (sum(a,b))
