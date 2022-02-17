# Lambda user
In order to let sls create an endpoint you need to create a user on IAM, with the following properties:
1. Choose any name for your user and select "Access key - Programmatic access" as AWS credential type
1. On the permissions section select "Attach existing policies directly" and select "Create policy"
1. On the Create Policy section choose to provide a json file and copy-paste the content of [iam_credentials.json](/doc/iam_credentials.json)
1. Once created, attach it to the user you are creating
1. Finish reviewing the user
1. Copy both the "Access Key ID" and "Access Secret Key", these will be AWS_ACCESS_KEY_ID and
AWS_SECRET_ACCESS_KEY, respectively
