num1 = int(input())
num2 = int(input())
num3 = int(input())
if(num1 >= num2):
    max = num1
else:
    max = num2
if(num3 >= max):
    max = num3
print(max)
