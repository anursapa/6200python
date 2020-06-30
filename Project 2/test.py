f = open("TestData.txt", "r")
linecount = 0
line = f.readline()
while line != "" and linecount < 100000:
    linecount = linecount + 1
    line = line.replace("\n","")
    linelist = line.split("\t")
   
    line = f.readline()
print(linelist)
#with open('TestData.txt') as file:
#    lines = file.readlines()
#    text = file.read()
#    test = text.replace('\n','\t')
#    lst = test.split('\t')

#print(len(lines))
#print(lines)
# i=0
# for s in lst:
#     lst[i]=s+'\t'
#     i=i+1
# lst2 = lst[0:46]
# newlist=[]

# for ii in range(len(lst)//23):
#     print(lst[13+ii*23:13+ii*23+5])
#     newlist.append(lst[13+ii*23:13+ii*23+5])
# i=0

# flat_list = [item for sublist in newlist for item in sublist]

# with open('soups.txt','w') as soupstxt:
#     soupstxt.writelines(flat_list)

# print(flat_list)
