# Import Needed Libraries
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from datetime import datetime
import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect('Nursapa.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
 
# if __name__ == '__main__':
#     create_connection("Nursapa.db")

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
        pass
    def buttonShowInputRowCountPressed(self):
        pass
    def buttonTableRowsCountPressed(self):
        pass
    def buttonListTablePressed(self):
        pass
    def buttonCustomSqlPressed(self):
        pass
    def buttonDistinctValuesPressed(self):
        pass
    
        
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
