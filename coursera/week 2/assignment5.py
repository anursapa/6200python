posKingX = int(input())
posKingY = int(input())
posNextX = int(input())
posNextY = int(input())
isValid1 = posKingX - posNextX
isValid2 = posKingY - posNextY
if(isValid1 >= -1 and isValid1 <= 1):
    if(isValid2 >= -1 and isValid2 <= 1):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
