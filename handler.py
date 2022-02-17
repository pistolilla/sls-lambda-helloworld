import json
import datetime

def response(body:dict, code:int=200):
    return {
        "statusCode": code,
        "headers": {
            "content-type": "application/json",
        },
        "body": json.dumps(body)
    }

def endpoint(event, context):
    """Returns a timestamp"""
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }
    return response(body)

def hello(event, context):
    """Returns the variables found in the request body"""
    data = json.loads(event["body"])
    return response(data)
