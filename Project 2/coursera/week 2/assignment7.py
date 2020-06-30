x = int(input())
y = int(input())
if(x == 1):
    print('Yes')
elif(y % (y - x + 1) == 0):
    print('YES')
else:
    print('No')
