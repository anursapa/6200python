a = int(input())
b = int(input())
c = int(input())
if (a > b + c) or (b > a + c) or (c > a + b):
    print('impossible')
elif((a * a == b * b + c * c) or (b * b == a * a + c * c) or
        (c * c == a * a + b * b)):
    print('rectangular')
elif((a * a > b * b + c * c) or (b * b > a * a + c * c) or
        (c * c > a * a + b * b)):
    print('obtuse')
else:
    print('acute')
