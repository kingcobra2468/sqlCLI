import sqlite3
import sys
import math
import time

class sqlMethods:  
    __databaseFile = None
    __databaseObject = None
    __databaseCursor = None

    def __init__(self, dbFile):
        self.__databaseFile = dbFile
        self.__databaseObject = sqlite3.connect(self.__databaseFile)
        self.__databaseCursor = self.__databaseObject.cursor()
    
    def fetchAllData(self, table):
        self.__databaseCursor.execute("SELECT * FROM " + table) #remember to input table once you get to it
        print(self.__databaseCursor.fetchall())

    def newTable(self, elements):
        listData = list(elements.split(' '))
        table = listData[0] #saves name of table
        elements = list()
        elementsStr = ""
        print(len(listData))
        print((len(listData)-1)%2)
        if (len(listData)-1)%2 == 0:
            for i in range(int(len(listData)-1)//2):
                elements.append([listData[(i * 2) + 1], listData[(i * 2) + 2]])
            time.sleep(5)
            for i in range(int(len(elements))):
                elementsStr += " " + str(elements[i][0]) + " " + str(elements[i][1]) + "," if (len(elements) -1) != i else " " + str(elements[i][0]) + " " + str(elements[i][1])
            print(elementsStr)
            self.__databaseObject.execute("CREATE TABLE " + table + "(" + elementsStr + ")")
            self.__databaseObject.commit()
    
    def insertIntoTable(self, elements):
        listData = list(elements.split(' '))
        table = listData[0]
        elementStr = ""
        for single in listData[1:]:
            elementStr += single + ", " if len(listData) - (listData.index(single) + 1) != 0 else single
        self.__databaseObject.execute("INSERT INTO " + table + " VALUES( " + elementStr + " )")
        self.__databaseObject.commit()

class runSQL(sqlMethods): 
    
    __input = None
    __options = None
    __optionsList = None
    
    def __init__(self, file):
        super().__init__(file)
    
    def interpreter(self):
        self.__input = ""
        self.__options = {'FA': self.fetchAllData, 'CT': self.newTable, 'IT': self.insertIntoTable}
        self.__optionsList = list(self.__options.keys())
        while self.__input != 'quit':
            self.__input = input(">> ")
            if self.__input == 'quit':
                break  
            else:
                pass
            i = 0
            while i < len(self.__optionsList):
                if str(self.__optionsList[i]) in self.__input:
                    break               
                else:
                    i+=1
                    continue
            #if self.__input not in self.__options:
                print('Invalid Input {}'.format(self.__input))
            self.__input = self.__input[len(self.__optionsList[i])+1:] 
            self.__options[self.__optionsList[i]](self.__input) #How to use dicts keys fo rep methods

sqlObject = runSQL(sys.argv[1])
sqlObject.interpreter()
del sqlObject