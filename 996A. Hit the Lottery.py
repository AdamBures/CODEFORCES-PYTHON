n = int(input())
ck = 0
while (n!=0):
    if n>= 100:
        n-=100
        ck+=1
    elif n>=20:
        n-=20
        ck+=1
    elif n>=10:
        n-=10
        ck+=1
    elif n>=5:
        n-=5
        ck+=1
    elif n>=1:
        n-=1
        ck+=1

print(ck)
