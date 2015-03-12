#!/usr/bin/env python
import ReadFile as readFile
import UpdateEntry as updateEntry
import GenerateReport as generator

menuList = ["Read file", "Export XML File", "Update User"]

i = 1;

print "Available options:"
for menuEntry in menuList:
    print i, menuEntry
    i+=1

selectedEntry = 0;

while ((selectedEntry <= 0) or (selectedEntry > len(menuList))):
    try:
        selectedEntry = int(raw_input("Please select an option from the menu "))
        if((selectedEntry <= 0) or (selectedEntry > len(menuList))):
            print "Not a valid option"
    except(ValueError):
        print "That's not a valid entry"

print "You have selected", menuList[selectedEntry - 1]

if (selectedEntry == 1):
    readFile.doSomething()

elif (selectedEntry == 3):
    updateEntry.doSomething()

elif (selectedEntry == 2):
    generator.printXml()
