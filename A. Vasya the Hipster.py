nums = list(map(int,input().split()))
a = nums[0]
b = nums[1]

if a >= b:
    a-= b
    a//=2
    print(f"{b} {a}")

else:
    b-= a
    b//= 2
    print(f"{a} {b}")
    
