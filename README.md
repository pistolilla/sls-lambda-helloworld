# sls-lambda-helloworld

Sample web service using AWS Lambda and [Serverless Framework](https://www.serverless.com/) (sls). This example was originally taken from [aws-python-simple-http-endpoint](https://github.com/serverless/examples/tree/v3/aws-python-simple-http-endpoint) tutorial

I. Make sure you have sls installed on your local machine. If not, follow [these instructions](/doc/serverless_installation.md)

II. Create an IAM user following [these instructions](/doc/lambda_user.md) and have both the Access Key Id and Secret Access Key for the next step

III. Deploy by running:
```bash
# Serverless deployment credentials
export AWS_ACCESS_KEY_ID=<your_key_here>
export AWS_SECRET_ACCESS_KEY=<your_secret_key_here>

sls deploy
```

IV. Use the endpoint(s) provided by the terminal
