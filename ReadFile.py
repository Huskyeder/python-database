from User import User
from DaoSqliteImpl import Dao

def doSomething():
    dao = Dao()
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
            dao.insertUsers(userList)
        else:
            print "file is empty"
    except IOError:
        print "File not Found"
