from User import User
import DaoSqliteImpl as dao

def doSomething():
    global dao
    userId = raw_input("Enter the employee id to update: ")
    user = findUserById(userId)
    if (user is None):
        print "User was not found"
    else:
        dao.printUser(userId)
        updateUser(user)

def findUserById(userId):
    return dao.findUserById(userId)

def updateUser(user):
    changes = False;
    newPhone = raw_input("Enter new phone. Leave blank if no changes:")
    newName = raw_input("Enter new Name. Leave blank if no changes: ")
    if (newPhone != ""):
        user.phoneNumber = newPhone
        changes = True
    if (newName != ""):
        user.name = newName
        changes = True
    if(changes):
        dao.saveUser(user)
