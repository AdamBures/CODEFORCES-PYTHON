n = int(input())
lst = []
count = 1
for i in range(n):
    mag = int(input())
    lst.append(mag)

for j in range(n-1):
    if lst[j] != lst[j+1]:
        count += 1


print(count)
