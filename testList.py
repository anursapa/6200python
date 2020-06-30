with open('testFile.txt') as textFile:
                text = textFile.read()
                #here we slpit the text into the list toList 
                toList = text.split()
                newList = []
                #using for loop we append to newList items
                #from toList which getting rid of non-alpha chars
                #such as &,?,' etc by joining alpha parts of a word
                for word in toList:
                    newList.append(''.join(alphaPart for alphaPart in word if alphaPart.isalpha()))
                #once we got the list of words containing only
                #alphabetic characters we can now convert the list
                #into a set to get unique values
                uniqueWordSet = set(newList)
                #since I always get a space as an item of newList we have to extract it from the set
                #we created and get the amount of unique words
                uniqueWordCountNum = len(uniqueWordSet)
                print(uniqueWordCountNum)
                print(newList)
