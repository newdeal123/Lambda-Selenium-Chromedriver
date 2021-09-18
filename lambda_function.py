from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import boto3,json


def lambda_handler(event, context):
    # TODO implement
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    chrome_options.binary_location = "/opt/python/bin/headless-chromium"
    driver = webdriver.Chrome('/opt/python/bin/chromedriver', chrome_options=chrome_options)
    print("driver arrive")
    driver.get('https://google.com') # enter your URL.

    parseBody=json.loads(event['body'])
    Bucket= "" # enter your S3 bucket.
    origin=parseBody['Item']['score_id']
    local='/tmp/'+origin

    s3=boto3.resource('s3')

    # download_file is a example. use your file name,format
    s3.Bucket(Bucket).download_file(origin+'.musicxml' , local+'.musicxml')

    print("file download done")

    ##################################################################
    #                                                                #
    #                                                                #
    #                       enter your code                          #
    #                                                                #
    #                                                                #
    ##################################################################

    s3.meta.client.upload_file(local+'.musicxml' , origin+'.musicxml')
    driver.close()
    return {
        "statusCode": 200,
        "body": json.dumps(parseBody,ensure_ascii=False)
    }
