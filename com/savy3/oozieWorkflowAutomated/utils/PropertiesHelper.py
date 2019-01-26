import xmltodict
with open('/Users/153665/Downloads/sqoop-automated/resources.xml') as fd:
    properties = xmltodict.parse(fd.read())["properties"]
    oozieProperties = properties["oozieProperties"]


def getSourceProperties(source):
    return properties["sourceProperties"][source]
