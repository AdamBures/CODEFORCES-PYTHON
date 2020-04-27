numbers = map(int, input().split())
lst = list(numbers)
lst2 = []
for i in lst:
    lst2.append(i)

lst2.sort()

a = lst2[3] - lst2[0]
b = lst2[3] - lst2[1]
c = lst2[3] - lst2[2] 

lst4 = []

lst4.insert(0,b)
lst4.insert(1,c)
lst4.insert(2,a)


print(lst4[0],lst4[1],lst4[2])
