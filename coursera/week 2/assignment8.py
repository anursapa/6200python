posX1 = int(input())
posY1 = int(input())
posX2 = int(input())
posY2 = int(input())
if((posX1 + posY1) % 2 == 0 and (posX2 + posY2) % 2 == 0):
    print('YES')
elif((posX1 + posY1) % 2 != 0 and (posX2 + posY2) % 2 != 0):
    print('YES')
else:
    print('NO')
