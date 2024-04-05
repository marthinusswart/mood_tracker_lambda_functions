import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    logger.info("Received a event: {}".format(event["body"]))
    print(event["body"])
    
    try:
        mood = json.loads(event["body"])
        logger.info("Received a mood JSON: {}".format(mood))
    except (KeyError, TypeError, ValueError):
        print("No JSON body or unable to parse JSON")
        mood = {}
    
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda!")
    }