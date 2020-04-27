numbers = list(map(int,input().split()))
numbers2 = list(map(int,input().split()))
count = 0
for i in range(len(numbers2)):
    if numbers2[i]>numbers[1]:
        count+=2

    else:
        count+=1

print(count)
