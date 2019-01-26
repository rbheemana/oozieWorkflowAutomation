import logging

def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info('Started')
    from com.savy3.oozieWorkflowAutomated.utils import PropertiesHelper
    logging.info(PropertiesHelper.envProperties['hive_url'])
    logging.info('Finished')

if __name__ == "__main__":
    main()