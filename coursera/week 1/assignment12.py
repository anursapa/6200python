priceDollars = int(input())
priceCents = int(input())
quantity = int(input())
totalDollars = priceDollars * quantity + (priceCents * quantity // 100)
totalCents = priceCents * quantity % 100
print(totalDollars, totalCents)
