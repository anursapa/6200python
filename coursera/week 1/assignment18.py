secondsPast = int(input())
hours = secondsPast // 60 // 60 % 24
minutes1 = secondsPast // 60 % 60 // 10
minutes2 = secondsPast // 60 % 60 % 10
seconds1 = secondsPast % 60 // 10
seconds2 = secondsPast % 60 % 10
print(hours, ":", minutes1, minutes2, ":", seconds1, seconds2, sep='')

