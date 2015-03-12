
class PropertiesReader:

    def __init__(self):
        f = open("system.properties")
        lines = f.readlines()
        self.dictionary = {}
        dictionary = {}
        for line in lines:
            elements = line.split("=")

            self.dictionary[elements[0]] = elements[1].rstrip('\n')
