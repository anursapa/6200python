n = int(input())
if(n % 10 == 1 and n != 11):
    print(n, 'korova')
elif(n >= 11 and n <= 14):
    print(n, 'korov')
elif((n % 10) >= 2 and (n % 10) <= 4):
    print(n, 'korovy')
else:
    print(n, 'korov')
