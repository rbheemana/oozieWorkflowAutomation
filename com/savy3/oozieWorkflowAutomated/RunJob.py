import logging

from com.savy3.oozieWorkflowAutomated.utils import BuildSqoopIngestParams


def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info('Started')
    logging.info('Getting Properties...In Progress...')
    BuildSqoopIngestParams.buildAndWriteJobProperties('full','mysql','orders','retail_db')
    logging.info('Finished')

if __name__ == "__main__":
    main()