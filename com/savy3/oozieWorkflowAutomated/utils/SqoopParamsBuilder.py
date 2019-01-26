from com.savy3.oozieWorkflowAutomated.utils import PropertiesHelper


def buildSqoopActionParams(ingestType,source,tablename, dbname):
    if ingestType == "full":
        return build_full_ingest_statement(source, tablename, dbname)

def build_full_ingest_statement(source, tablename, dbname):
    envvars = PropertiesHelper.getSourceProperties(source)
    sqoopArgs = dict()
    sqoopArgs['connect'] = envvars['jdbcUrl'] + "/" + dbname
    sqoopArgs['username'] = envvars['jdbcUsername']
    sqoopArgs['password-file'] = envvars['jdbcPasswordFilePath']
    sqoopArgs['table'] = tablename
    sqoopArgs['target-dir'] = envvars['hdfsSqoopImportLocation'] + "/" + dbname + "/" + tablename
    sqoopArgs['num-mappers'] = envvars['mappers']
    return 'import ' + ' '.join("--{} {}".format(key, val) for (key, val) in sqoopArgs.items())