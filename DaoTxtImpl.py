from User import User
import ReadFile as readFile

def init():
    global connection
    connection = open("database.txt")
    return connection

def findUserById(userId):
        connection = init()
        lines = connection.readlines()
        user = None
        for line in lines:
            properties = line.split(",")
            if properties[0] == userId:
                user = User(properties[0], properties[1], properties[2], properties[3], properties[4])
                break
        return user

def printUser(userId):
    userToPrint = findUserById(userId)

    print "Name: %s " % userToPrint.name
    print "Age: %s" % userToPrint.age
    print "Birthday: %s " % userToPrint.birthday
    print "Phone number: %s" % userToPrint.phoneNumber

def getUsers():
    return readFile.getUsers()

def saveUser(user):
    connection = init()
    print "Saving user"
