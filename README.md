# Lambda-Selenium-Chromedriver
Setting up the Selenium,Chromedriver environment in AWS Lambda.   
lambda_function.py contains the process of downloading the file from S3, completing the work through Cellinium in a chrome environment, and uploading the file back to S3.   

---
### 1. Copy lambda_function.py and paste it into your lambda function.
### 2. Do not release the two zip files(chromedriver.zip, selenium.zip) in the layer folder, add them to the lambda layer, respectively, and apply them to the lambda function.
### 3. Check that the test is successful after changing the lambda function to suit your logic.
### 4. If successful, tap Star⭐️ in this repository. Yeah!

### cf. runtime support Python 3.6 & 3.7
