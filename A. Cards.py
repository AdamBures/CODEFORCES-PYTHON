number = int(input())
word = str(input())
result = ""


for i in word:
    if i == "z":
        result += "0"
    elif i == "n":
        result += "1"

lst = []
for j in result:
    lst.append(int(j))
    lst.sort(reverse=True)

result2 = ""

for k in lst:
    result2 += str(k) + " "
    
print(result2)
