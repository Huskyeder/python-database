from User import User
import DaoSqliteImpl as dao

def doSomething():
    try:
        f = open("input.csv")
        lines = f.readlines()
        userList = []
        for line in lines:
            properties = line.split(",")
            newUser = User()
            setattr(newUser, "id", properties[0].strip())
            setattr(newUser, "name", properties[1].strip())
            setattr(newUser, "age", properties[2].strip())
            setattr(newUser, "phoneNumber", properties[3].strip())
            setattr(newUser, "birthday", properties[4].rstrip("\n"))
            userList.append(newUser)

            if (userList):
                insertUsers(userList)
            else:
                print "file is empty"
    except IOError:
        print "File not Found"

def insertUsers(userList):
    dao.insertUsers(userList)

def getUsers():
    f = open("import.txt")
    lines = f.readlines()

    userList = []
    for line in lines:
        properties = line.split(",")
        newUser = User(properties[0], properties[1], properties[2], properties[3], properties[4])
        userList.append(newUser)
    return userList;
