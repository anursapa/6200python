import time as t
from os import path

def createFile(dest):
    '''
    The script creates a text a text file at
    the past in location names file based on date
    '''
    date=t.localtime(t.time())

    #FileName = Month_Day_Year
    name='%d_%d_%d.txt'%(date[1],date[2],(date[0]%100))

    if not(path.isfile(dest+name)):
        f=open(dest+name,'w')
        f.write('\n'*30)
        f.close()
if __name__=='__main__':
    destination='C:\\Users\\User\\Desktop\\6200 Introduction to python\\testing\\'
    createFile(destination)
    raw_input('done!!!')
