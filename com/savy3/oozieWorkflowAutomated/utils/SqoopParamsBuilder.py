from com.savy3.oozieWorkflowAutomated.utils import PropertiesHelper


def buildSqoopActionParams(ingestType,source):
    if ingestType == "incr":
        PropertiesHelper.getSourceProperties(source)