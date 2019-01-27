import xmltodict, os, logging

#resources.xml
resourceFilePath = os.path.abspath("../../../resources.xml")
logging.info("Reading parameters from the path : %s",resourceFilePath)

with open(resourceFilePath) as fd:
    properties = xmltodict.parse(fd.read())["properties"]
    oozieProperties = properties["oozieProperties"]
    envProperties = properties["envProperties"]

def getSourceProperties(source):
    return properties["sourceProperties"][source]



def dictToPropString(temp):
    if temp != None:
        return '\n'.join("{}={}".format(key, val) for (key, val) in temp.items())
    else:
        return ""

# if __name__ == "__main__":
#     print(dictToPropString(envProperties))