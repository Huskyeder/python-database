import xml.etree.cElementTree as ET
import DaoSqliteImpl as dao
from PropertiesReader import PropertiesReader
from datetime import datetime
import os

def printXml():
    properties = PropertiesReader()
    userList = dao.getUsers()
    root = ET.Element("xml")

    recordUpdated = ET.SubElement(root, "agenda")

    for user in userList:
        person = ET.SubElement(recordUpdated, "person")
        personId = ET.SubElement(person, "id").text = str(user.id)
        personName = ET.SubElement(person, "name").text = user.name
        personAge = ET.SubElement(person, "age").text = user.age
        personPhoneNumber = ET.SubElement(person,"phone_number").text = user.phoneNumber
        birthDate = datetime.strptime(user.birthday, "%Y-%m-%d")
        personBirthDate = ET.SubElement(person, "birthday")
        personBirthday = ET.SubElement(personBirthDate, "day").text = str(birthDate.day)
        personBirthMonth = ET.SubElement(personBirthDate, "month").text = str(birthDate.month)
        personBirthYear = ET.SubElement(personBirthDate, "year").text = str(birthDate.year)

    tree = ET.ElementTree(root)
    filename = properties.dictionary["XML_FILENAME"]
    directory = os.path.dirname(filename)
    noDir = directory == ""
    if not noDir:
        if not os.path.exists(directory):
            os.makedirs(directory)

    tree.write(filename)
    print "XML printed as:", filename
