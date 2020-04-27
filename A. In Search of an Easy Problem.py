three = int(input())
number = map(int, input().split())
lst = list(number)
if 1 in lst:
    print("HARD")
else:
    print("EASY")
