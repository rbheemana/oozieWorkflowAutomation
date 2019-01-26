import xmltodict
import os
os.chdir(os.path.dirname(__file__))
resourceFilePath = os.path.abspath("../../../../resources.xml")
with open(resourceFilePath) as fd:
    properties = xmltodict.parse(fd.read())["properties"]
    oozieProperties = properties["oozieProperties"]
    envProperties = properties["envProperties"]

def getSourceProperties(source):
    return properties["sourceProperties"][source]
