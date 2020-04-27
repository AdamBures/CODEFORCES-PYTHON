num = int(input())
commands = str(input())
x = 0
lst = [0]

for i in commands:
    if i == "L":
        x-=1
        lst.append(x)
    else:
        x+=1
        lst.append(x)
    
print(len(lst))
