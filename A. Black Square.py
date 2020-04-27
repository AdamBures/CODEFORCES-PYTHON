n = list(map(int,input().split()))
s = input()
result = s.count("1")*n[0]+s.count("2")*n[1]+s.count("3")*n[2]+s.count("4")*n[3]
print(result)
