from User import User
from DaoSqliteImpl import  Dao

def doSomething():
    dao = Dao()
    userId = raw_input("Enter the employee id to update: ")
    user = findUserById(dao,userId)
    if (user is None):
        print "User was not found"
    else:
        dao.printUser(userId)
        updateUser(dao,user)

def findUserById(dao,userId):
    return dao.findUserById(userId)

def updateUser(dao,user):
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
