from com.savy3.oozieWorkflowAutomated.utils import PropertiesHelper


def main():
    print(PropertiesHelper.properties['env']['hive_url'])


if __name__ == "__main__":
    main()