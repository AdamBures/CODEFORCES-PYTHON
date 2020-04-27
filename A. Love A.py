string = str(input())
ac = 0
n = len(string)
for i in range(n):
    if string[i] == "a":
        ac+= 1

while(ac<=n/2):
    n-=1  
print(n)
