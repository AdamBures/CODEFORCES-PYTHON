n = int(input())
oddString = "I hate "
evenString = "I love "
endingLetter1 = "it"
endingLetter2 = "that "
result = ""
for i in range(1,n+1):
    if i%2 == 0:
        result += evenString
        if i==n:
            result += endingLetter1
        else:
            result += endingLetter2
    else:
        result += oddString
        if i==n:
            result += endingLetter1
        else:
            result += endingLetter2
print(result)
