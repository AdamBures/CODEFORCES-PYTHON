dividing_number = int(input())
numbers = map(int,input().split())
lst = []

for i in numbers:
    lst.append(i)
a = sum(lst)/100

print(round((a/dividing_number)*100,12))
