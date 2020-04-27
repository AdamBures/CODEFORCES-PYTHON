n = int(input())
lst = []
for i in range(n):
    word = str(input())
    lst.append(word)

for j in lst:
    string = len(j) - 1
    if j[string-1] == 'p' and j[string] == 'o':
        print("FILIPINO")
    elif j[string-3] == "d" and j[string-2] == "e" and j[string-1] == "s" and j[string] == "u":
        print("JAPANESE")
    elif j[string-3] == "m" and j[string-2] == "a" and j[string-1] == "s" and j[string] == "u":
        print("JAPANESE")
    elif j[string-4] == "m" and j[string-3] == "n" and j[string-2] == "i" and j[string-1] == "d" and j[string] == "a":
        print("KOREAN")
