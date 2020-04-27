numbers = map(int, input().split())

lst = list(numbers)

participant = lst[0]
pens = lst[1]
notebooks = lst[2]

if participant <= pens and participant <= notebooks:
    print("Yes")
else:
    print("No")
