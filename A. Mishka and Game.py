n = int(input())
mishka = 0
criss = 0

for i in range(n):
    game = list(map(int,input().split()))
    if game[0] > game[1]:
        mishka +=1
    elif game[0]<game[1]:
        criss+=1

if mishka > criss:
    print("Mishka")
elif criss > mishka:
    print("Chris")

else:
    print("Friendship is magic!^^")
