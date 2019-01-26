from com.savy3.oozieWorkflowAutomated.utils import PropertiesHelper, SqoopParamsBuilder
import logging, os

def writeJobProperties(jobPropertiesPath,dynamicDict):
    with open(jobPropertiesPath, 'w') as job:
        lines = list()
        envProperties = PropertiesHelper.dictToPropString(PropertiesHelper.env)
        oozieProperties = PropertiesHelper.dictToPropString(PropertiesHelper.oozieProperties)
        dynamicProperties = PropertiesHelper.dictToPropString(dynamicDict)
        job.writelines(envProperties+"\n"+oozieProperties+"\n"+dynamicProperties)


def buildAndWriteJobProperties(ingestType,source,tablename, dbname)
    dynamicDict = dict()
    dynamicDict['query'] = SqoopParamsBuilder.buildSqoopActionParams(ingestType,source,tablename, dbname)
    jobPropertiesPath = os.path.abspath("../../../../target/wf_sqoop_ingest/job.properties")
    logging.info("Writing parameters to the path : %s", jobPropertiesPath)
    writeJobProperties(jobPropertiesPath, dynamicDict)
