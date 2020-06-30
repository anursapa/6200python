# Import Needed Libraries
import sys
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import datetime


conn = sqlite3.connect('Nursapa.db')
cursor = conn.cursor()
cursor.executescript("""
drop table if exists Days;
create table Days (
DoY int Primary key not null,
DoW text,
Holiday int,
Weather text);\
drop table if exists Managers;
create table Managers (
MgrId int Primary key not null,
MgrName text,
Grade text,
Years int);
drop table if exists Promotions;
create table Promotions (
PromoId int Primary key not null,
Medium text,
Target text,
Interval text);
drop table if exists Soups;
create table Soups (
SoupId int Primary key not null,
Type text,
Vendor text,
Mode text,
Style text);
drop table if exists Stores;
create table Stores (
StoreId int Primary key not null,
Location text,
Size text,
Elevation text,
MgrId int);
drop table if exists sales;
create table sales (
TrxId int Primary key not null,
DoY int,
StoreID int,
SoupId int,
PromoId int,
Sales number);
""")
conn.commit()

class Form( QDialog):
    # Form Constructor
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        cryptokey = 50
        self.pbuttonName = QPushButton("Developer's Name")
        self.lineeditName = QLineEdit("")
        self.pbuttonSemester = QPushButton("Current Semester")
        self.lineeditSemester = QLineEdit("")
        self.pbuttonLoadFile = QPushButton("Load File")
        self.lineeditLoadFile = QLineEdit("Enter Input File Name")
        self.pbuttonShowInputRowCount = QPushButton("Show Input Row Count")
        self.lineeditShowInputRowCount = QLineEdit("Total Input Rows Parsed")
        self.pbuttonTableRowsCount = QPushButton("Table rows count")
        self.lineeditTableRowsCount = QLineEdit("Enter table name")
        self.pbuttonListTable = QPushButton("List table")
        self.lineeditListTable = QLineEdit("Enter table name")
        self.pbuttonCustomSql = QPushButton("Custom Sql")
        self.lineeditCustomSql = QLineEdit("Enter custom sql")
        self.pbuttonDistinctValues = QPushButton("Distinct values")
        self.lineeditDistinctValues = QLineEdit("Enter table name, column name")
        self.pbuttonQuit = QPushButton("Quit")              
        # self.labelSelectFunction = QLabel("Select a Function")
        # self.pbuttonCharacterCount = QPushButton("Character Count")
        # self.lineeditCharacterCount = QLineEdit("")
        # self.pbuttonLineCount = QPushButton("Line Count")
        # self.lineeditLineCount = QLineEdit("")
        # self.pbuttonUniqueWordCount = QPushButton("Unique Word Count")
        # self.lineeditUniqueWordCount = QLineEdit("")
        # self.pbuttonCharactersPerWord = QPushButton("Average Characters Per Word")
        # self.lineeditCharactersPerWord = QLineEdit("")
        # self.texteditTextBox = QTextEdit('Text will be shown here')
        # self.pbuttonQuit = QPushButton("Quit")
        layout = QVBoxLayout() 
        layout.addWidget(self.pbuttonName)
        layout.addWidget(self.lineeditName)
        layout.addWidget(self.pbuttonSemester)
        layout.addWidget(self.lineeditSemester)       
        layout.addWidget(self.pbuttonLoadFile)
        layout.addWidget(self.lineeditLoadFile)
        layout.addWidget(self.pbuttonShowInputRowCount)
        layout.addWidget(self.lineeditShowInputRowCount)
        layout.addWidget(self.pbuttonTableRowsCount)
        layout.addWidget(self.lineeditTableRowsCount)
        layout.addWidget(self.pbuttonListTable)
        layout.addWidget(self.lineeditListTable)
        layout.addWidget(self.pbuttonCustomSql)
        layout.addWidget(self.lineeditCustomSql)
        layout.addWidget(self.pbuttonDistinctValues)
        layout.addWidget(self.lineeditDistinctValues)
        layout.addWidget(self.pbuttonQuit)
        self.setLayout(layout)
        ck = cryptokey
        self.pbuttonName.setFocus()
        self.connect(self.pbuttonName, SIGNAL("clicked()"),self.buttonNamePressed)
        self.connect(self.pbuttonSemester, SIGNAL("clicked()"),self.buttonSemesterPressed)
        self.connect(self.pbuttonLoadFile, SIGNAL("clicked()"),self.buttonLoadFilePressed)
        self.connect(self.pbuttonShowInputRowCount, SIGNAL("clicked()"),self.buttonShowInputRowCountPressed)
        self.connect(self.pbuttonTableRowsCount, SIGNAL("clicked()"),self.buttonTableRowsCountPressed)
        self.connect(self.pbuttonListTable, SIGNAL("clicked()"),self.buttonListTablePressed)
        self.connect(self.pbuttonCustomSql, SIGNAL("clicked()"),self.buttonCustomSqlPressed)
        self.connect(self.pbuttonDistinctValues, SIGNAL("clicked()"),self.buttonDistinctValuesPressed)
        self.connect(self.pbuttonQuit, SIGNAL("clicked()"),self.buttonQuitPressed)
        s = chr(ck + 20) + chr(ck) + chr(ck-2) +chr(ck-1)+chr(ck+6)
        self.setWindowTitle(s)
    
    def buttonNamePressed(self):
        def WhoAmI():
            return ('Arsultan Nursapa')
        
        self.lineeditName.setText(WhoAmI())
    def buttonSemesterPressed(self):
        def CurrentSemester():
            month = datetime.now().month
            year = datetime.now().year
            if ((month >=8) and (month <= 12)):
                semester = 'F'+str(year)
                return(semester)
            elif((month>=6) and (month<=7)):
                semester = 'Summer'+str(year)
                return(semester)
            else:
                semester = 'S'+str(year)
                return(semester)

        self.lineeditSemester.setText(CurrentSemester())
    
    def buttonLoadFilePressed(self):
        global fileName
        fileName = self.lineeditLoadFile.text()
        def loadFile():    
            def insertData(record):
                try:
                    conn = sqlite3.connect('Nursapa.db')
                    cursor = conn.cursor()
                    TrxId = int(record[0])
                    DoY = int(record[1])
                    DoW = str(record[2])
                    Holiday = str(record[3])
                    Weather = str(record[4]) 
                    StoreId = int(record[5])
                    Location = str(record[6])
                    Elevation = str(record[7])
                    Size  = str(record[8])
                    MgrId = int(record[9])
                    MgrName = str(record[10])
                    Grade = str(record[11])
                    Years = int(record[12])
                    SoupId = int(record[13])
                    Type = str(record[14])
                    Vendor = str(record[15])
                    Mode = str(record[16])
                    Style = str(record[17])
                    PtomoId = int(record[18])
                    Medium = str(record[19])
                    Target =str(record[20])
                    Interval = str(record[21])
                    Sales = float(record[22])
                    rowSales = [TrxId,DoY,StoreId,SoupId,PtomoId,Sales] #6
                    rowDays = [DoY,DoW,Holiday,Weather] #4
                    rowStores = [StoreId,Location,Elevation,Size,MgrId] #5
                    rowManagers = [MgrId,MgrName,Grade,Years] # 4
                    rowSoups = [SoupId, Type,Vendor,Mode,Style] #5
                    rowPromos = [PtomoId,Medium,Target,Interval] #4
                    cursor.execute("INSERT or ignore INTO Days VALUES(?, ?, ?,?)", rowDays)
                    cursor.execute("INSERT or ignore INTO Sales VALUES(?, ?, ?,?,?,?)", rowSales)
                    cursor.execute("INSERT or ignore INTO Stores VALUES(?, ?, ?, ?, ?)", rowStores)
                    cursor.execute("INSERT or ignore INTO Managers VALUES(?, ?, ?,?)", rowManagers)
                    cursor.execute("INSERT or ignore INTO Promotions VALUES(?, ?, ?,?)", rowPromos)
                    cursor.execute("INSERT or ignore INTO Soups VALUES(?, ?, ?,?,?)", rowSoups)
                    conn.commit()
                except sqlite3.Error as er:
                    print 'er:', er.message
            try:
                f=open(fileName, "r")
                linecount = 0
                line = f.readline()
                while line != "" and linecount < 65000:
                    linecount = linecount + 1
                    line = line.replace("\n","")
                    linelist = line.split("\t")
                    insertData(linelist)
                    line = f.readline()
                return('File Parsed')
            except IOError:
                return ("File Not Found")
            print(linelist)
        self.lineeditLoadFile.setText(loadFile())
    def buttonShowInputRowCountPressed(self):
        def countInputRows():
            try:
                with open(str(fileName)) as textFile:
                    rows = textFile.readlines()
                return(len(rows))
            except NameError:
                return('File is not specified')
            except IOError:
                return('File not found')

        self.lineeditShowInputRowCount.setText(str(countInputRows()))

    def buttonTableRowsCountPressed(self):
        tableName = self.lineeditTableRowsCount.text()
        conn = sqlite3.connect('Nursapa.db')
        cursor = conn.cursor()
        cursor.execute('select count(*) from %s' %tableName)
        count = cursor.fetchall()[0][0]
        self.lineeditTableRowsCount.setText(str(count))

    def buttonListTablePressed(self):
        tableName2 = self.lineeditListTable.text()
        conn = sqlite3.connect('Nursapa.db')
        cur = conn.cursor()
        cur.execute ("Select * from %s" %tableName2)
        if (tableName2.toLower() == "sales"):
            print ('TrxID' + "\t" + 'DoY' + "\t" + 'StoreId' + "\t" + 'SoupId' + "\t" + 'PromoId' + "\t" + 'Sales' + "\n")
            for row in cur:
                print (str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[4]) + "\t" + str(row[5]) + "\n")
        if (tableName2.toLower() == 'days'):
            print ('DoY' + "\t" + 'DoW' + "\t" + 'Holiday' + "\t" + 'Weather' + "\n")
            for row in cur:
                print (str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\n")
        if (tableName2.toLower()=='managers'):
            print ('MgrId' + "\t" + 'MgrNamne' + "\t" + 'Grade' + "\t" + 'Years' + "\n")
            for row in cur:
                print (str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\n")
        if (tableName2.toLower()== 'promotions'):
            print ('PromoId' + "\t" + 'Medium' + "\t" + 'Target' + "\t" + 'Interval' + "\n")
            for row in cur:
                print (str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\n")
        if (tableName2.toLower()== 'soups'):
            print ('SoupId' + "\t" + 'Type' + "\t" + 'Vendor' + "\t" + 'Mode' + "\t" + 'Style' + "\n")
            for row in cur:
                print (str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[4]) + "\n")
        if (tableName2.toLower()== 'stores'):
            print ('StoreId' + "\t" + 'Location' + "\t" + 'Size' + "\t" + 'Elevation' + "\t" + 'MgrId' + "\n")
            for row in cur:
                print (str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[4]) + "\n")
        self.lineeditListTable.setText('Printed in IDLE shell')
    
    def buttonCustomSqlPressed(self):
        customSql = self.lineeditCustomSql.text()
        conn = sqlite3.connect('Nursapa.db')
        cur = conn.cursor()
        cur.execute(str(customSql))
        result = cur.fetchall()
        print(result)
        self.lineeditCustomSql.setText('Executed')
        
    def buttonDistinctValuesPressed(self):
        distinct = self.lineeditDistinctValues.text()
        lst = distinct.split(',')
        tableD = lst[0]
        columnD = lst[1]
        conn = sqlite3.connect('Nursapa.db')
        cur = conn.cursor()
        cur.execute ("select distinct %s from %s" % (columnD, tableD))
        x = cur.fetchall()
        self.lineeditDistinctValues.setText(str(len(x)) + ' unique values')
    
        
    # def buttonOpenFilePressed(self):
    #     #define a global variable fileName as we will need it in all functions
    #     global fileName
    #     fileName = self.lineeditOpenFile.text()
    #     #try-except construction helps to avoid IOError and print out 'File opened' or 'File Not Found'
    #     def OpenFile():
    #         #I used the try-except construction from the youtube video you provided us during week 5
    #         try:
    #             f=open(fileName, "r")
    #             text = f.read()
    #             self.texteditTextBox.setText(text) 
    #             return('File Opened')
    #         except IOError:
    #             return ("File Not Found")
           
    #     self.lineeditOpenFile.setText(OpenFile())
    # def buttonCharacterCountPressed(self):
    #     def characterCount():
    #         try:
    #             with open(str(fileName)) as textFile:
    #                 #with .read() method we read a file and store the data in the variable text as a string
    #                 text = textFile.read()
    #                 #here create a list of charachters(using a definite loop) of the text which are alphabetic using .isalpha() method 
    #                 alphaCharacterList = [characterAlpha for characterAlpha in text if characterAlpha.isalpha()]
    #                 # amount of alphabetic characters will be equal to the length of the list
    #                 alphaCharacterAmount = len(alphaCharacterList)
    #                 '''
    #                 there is one more way I know how to doit:
    #                 alphatext=''.join(alpha for alpha in text if alpha.isalpha())
    #                 alphaCharacterCount = len(alphatext)
    #                 '''
    #                 return(alphaCharacterAmount)
    #         except NameError:
    #             return('File is not specified')
    #         except IOError:
    #             return('File not found')            
    #     self.lineeditCharacterCount.setText(str(characterCount()))

    # def buttonLineCountPressed(self):
    #     #this was explained in the class
    #     def lineCount():
    #         try:
    #             with open(str(fileName)) as textFile:
    #                 lineAmount = 0
    #                 line = textFile.readline()
    #                 while line != '':
    #                     lineAmount = lineAmount + 1
    #                     line = textFile.readline()
    #                 return (lineAmount)
    #         except NameError:
    #             return('File is not specified')
    #         except IOError:
    #             return('File not found') 
    #     self.lineeditLineCount.setText(str(lineCount()))

    # def buttonUniqueWordCountPressed(self):
    #     def uniqueWordCount():
    #         try:
    #             with open(str(fileName)) as textFile:
    #                 text = textFile.read()
    #                 #here we slpit the text into the list toList converting all the letters to lowercase to count unique words since 'Word' is not equal 'word'
    #                 toList = text.lower().split()
    #                 newList = []
    #                 #using for loop we append to newList items
    #                 #from toList which getting rid of non-alpha chars
    #                 #such as &,?,',0-9 etc by joining alpha parts of a word. We get the list of alpha words
    #                 for word in toList:
    #                     newList.append(''.join(alphaPart for alphaPart in word if alphaPart.isalpha()))
    #                 #since I always get a space as an item of newList(due to having numbers in list which result to an empty item)
    #                 #we have to get rid of empty items
    #                 while '' in newList:
    #                     newList.remove('')
    #                 #once we got the list of words containing only
    #                 #alphabetic characters we can now convert the list
    #                 #into a set to get unique values
    #                 uniqueWordNum = len(set(newList))
    #                 return(uniqueWordNum)
    #         except NameError:
    #             return('File is not specified')
    #         except IOError:
    #             return('File not found') 
    #     self.lineeditUniqueWordCount.setText(str(uniqueWordCount()))

    # def buttonCharactersPerWordPressed(self):
    #     def charactersPerWord():
    #         try:
    #             with open(str(fileName)) as textFile:
    #                 text = textFile.read()
    #                 toList = text.split()
    #                 charactersPerWordNum = float(len(''.join(toList)))/float(len(toList))

    #                 '''
    #                 This is the way to calculate characters per word assuming we take only alpha chars
    #                 newList = []
    #                 #using for loop we append to newList items
    #                 #from toList which getting rid of non-alpha chars
    #                 #such as &,?,',0-9 etc by joining alpha parts of a word. We get the list of alpha words
    #                 for word in toList:
    #                     newList.append(''.join(alphaWord for alphaWord in word if alphaWord.isalpha()))
    #                 #getting rid of empty items in the list so we can get a proper list of words which then will help us to count totalwords
    #                 while '' in newList:
    #                     newList.remove('')
    #                 #now we need to get the total amount of characters by joining all the strings from the list
    #                 totalChars = len(''.join(newList))
    #                 #we count the total amount of words in in the list
    #                 totalWords = len(newList)
    #                 #I assume that the amount of characters per word would be equal to the division of the
    #                 #amount of alphabetic letters and the amount of words containg only alphabetic characters
    #                 charactersPerWordNum = float(totalChars)/float(totalWords)
    #                 return(charactersPerWordNum)
    #                 '''
    #                 return(charactersPerWordNum)
    #         except NameError:
    #             return('File is not specified')
    #         except IOError:
    #             return('File not found') 
    #     self.lineeditCharactersPerWord.setText(str(charactersPerWord()))

    def buttonQuitPressed(self):
        self.done(1)
        app.quit()
# End of Form Class Definition

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
