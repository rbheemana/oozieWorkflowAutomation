from com.savy3.oozieWorkflowAutomated.utils import PropertiesHelper


def main():
    print(PropertiesHelper.envProperties['hive_url'])


if __name__ == "__main__":
    main()