# sls-lambda-helloworld

Sample web service using AWS Lambda and [Serverless Framework](https://www.serverless.com/) (sls). This example was taken from [aws-python-simple-http-endpoint](https://github.com/serverless/examples/tree/v3/aws-python-simple-http-endpoint)

I. Make sure you have sls installed. If not, follow [these instructions](/doc/serverless_installation.md)

II. Create an IAM user following [these instructions](/doc/lambda_user.md)

III. Deploy by running:
```bash
# Serverless deployment credentials
export AWS_ACCESS_KEY_ID=<your_key_here>
export AWS_SECRET_ACCESS_KEY=<your_secret_key_here>

sls deploy
```

IV. Navigate to the endpoint provided by the terminal
