from User import User
from PropertiesReader import PropertiesReader
import sqlite3
class Dao:
    def __init__(self):
        self.properties = PropertiesReader()
        self.connection = sqlite3.connect(self.properties.dictionary["DATABASE_NAME"])
        self.connection.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE
           (id INT PRIMARY KEY     NOT NULL,
            name NOT NULL,
            age  NOT NULL,
            phone_number,
            birthday );''')
        self.connection.text_factory = str

    def findUserById(self,userId):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM EMPLOYEE WHERE id = '%s'" % userId)
        uTuple = cursor.fetchone()
        if (uTuple == None):
            return None
        else:
            foundUser = User()
            setattr(foundUser, "id", uTuple[0])
            setattr(foundUser, "name", uTuple[1])
            setattr(foundUser, "age", uTuple[2])
            setattr(foundUser, "phoneNumber", uTuple[3])
            setattr(foundUser, "birthday", uTuple[4])
            return foundUser

    def printUser(self,userId):
        userToPrint = self.findUserById(userId)
        if not (userToPrint is None):
            print "Name: %s " % userToPrint.name
            print "Age: %s" % userToPrint.age
            print "Birthday: %s " % userToPrint.birthday
            print "Phone number: %s" % userToPrint.phoneNumber

    def getUsers(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM EMPLOYEE")
        userTupleList = cursor.fetchall()
        userList = []
        for userTuple in userTupleList:
            user = User()
            setattr(user, "id", userTuple[0])
            setattr(user, "name", userTuple[1])
            setattr(user, "age", userTuple[2])
            setattr(user, "phoneNumber", userTuple[3])
            setattr(user, "birthday", userTuple[4])
            userList.append(user)
        return userList

    def saveUser(self,user):
        cursor = self.connection.cursor()
        self.connection.execute( "UPDATE EMPLOYEE SET name = '%s', phone_number = '%s' WHERE id = %s" % (user.name, user.phoneNumber,user.id))
        self.connection.commit()

    def insertUsers(self, userList):
        cursor = self.connection.cursor()
        for user in userList:
            try:
                self.connection.execute ( "INSERT INTO EMPLOYEE(id, name, age, phone_number, birthday) VALUES('%s','%s','%s','%s','%s') " %(user.id,user.name, user.age, user.phoneNumber, user.birthday))
                print "adding:", user.id,user.name
            except sqlite3.IntegrityError:
                print "id:", user.id,"already in database. User not added."
        self.connection.commit()

    def closeConnection(self):
        self.connection.close()
