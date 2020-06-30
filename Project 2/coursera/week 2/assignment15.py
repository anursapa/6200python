a = int(input())
b = int(input())
c = int(input())
x1 = a % 2
x2 = b % 2
x3 = c % 2
if x1 == 0 and x2 != 0:
    print("YES")
elif x1 == 0 and x3 != 0:
    print("YES")
elif x2 == 0 and x1 != 0:
    print("YES")
elif x2 == 0 and x3 != 0:
    print("YES")
elif x3 == 0 and x1 != 0:
    print("YES")
elif x3 == 0 and x2 != 0:
    print("YES")
else:
    print("NO")
