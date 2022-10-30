import json
from pathlib import Path
from selenium import webdriver
from tempfile import mkdtemp


CHROMEDRIVER_PATH = '/opt/chromedriver'
CHROME_BIN = '/opt/google/chrome/chrome'


def get_driver():
    options = webdriver.ChromeOptions()

    options.binary_location = CHROME_BIN

    '''
    lambda: selenium.common.exceptions.WebDriverException: Message: unknown error: unable to discover open window in chrome
    locally: works fine
    '''
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1280x1696")
    # options.add_argument("--single-process")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-dev-tools")
    # options.add_argument("--no-zygote")
    # options.add_argument(f"--user-data-dir={mkdtemp()}")
    # options.add_argument(f"--data-path={mkdtemp()}")
    # options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    # options.add_argument("--remote-debugging-port=9222")

    '''chrome crashes right from start on lambda, works fine locally'''
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-gpu')
    options.add_argument("window-size=1400,800")

    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, chrome_options=options)

    return driver

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }
