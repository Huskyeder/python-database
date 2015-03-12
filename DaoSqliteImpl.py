from User import User
from PropertiesReader import PropertiesReader
import sqlite3

def init():
    properties = PropertiesReader()
    connection = sqlite3.connect(properties.dictionary["DATABASE_NAME"])
    connection.text_factory = str
    return connection

def findUserById(userId):
    c = init().cursor()
    c.execute("SELECT * FROM EMPLOYEE WHERE id = '%s'" % userId)
    uTuple = c.fetchone()
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

def printUser(userId):
    userToPrint = findUserById(userId)

    print "Name: %s " % userToPrint.name
    print "Age: %s" % userToPrint.age
    print "Birthday: %s " % userToPrint.birthday
    print "Phone number: %s" % userToPrint.phoneNumber

def getUsers():
    conn = init()
    c = conn.cursor()
    c.execute("SELECT * FROM EMPLOYEE")
    userTupleList = c.fetchall()
    userList = []
    for userTuple in userTupleList:
        user = User(userTuple[0], userTuple[1], userTuple[2], userTuple[3], userTuple[4])
        userList.append(user)
    return userList

def saveUser(user):
    conn = init()
    cursor = conn.cursor()
    conn.execute( "UPDATE EMPLOYEE SET name = '%s', phone_number = '%s' WHERE id = %s" % (user.name, user.phoneNumber,user.id))
    conn.commit()

def insertUsers(userList):
    conn = init()
    cursor = conn.cursor()
    for user in userList:
        try:
            conn.execute ( "INSERT INTO EMPLOYEE(id, name, age, phone_number, birthday) VALUES('%s','%s','%s','%s','%s') " %(user.id,user.name, user.age, user.phoneNumber, user.birthday))
        except sqlite3.IntegrityError:
            print "id:", user.id,"already in database. User not added."
    conn.commit()
