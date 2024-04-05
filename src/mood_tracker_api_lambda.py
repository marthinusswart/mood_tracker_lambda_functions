import json
import logging
import boto3
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3_bucket = "aws-applications-and-services"
server_details_key = "mood-tracker-app/mood-data"

def generate_s3_file_name() -> str:
  current_datetime = datetime.datetime.now()
  formatted_now = current_datetime.strftime("%Y-%m-%d-%H-%M-%S")
  filename = "mood_item_{}.json".format(formatted_now)
  return filename

def store_mood_item(mood) -> str:
   s3_filename = generate_s3_file_name()
   s3 = boto3.client("s3") 
   s3.put_object(Body=json.dumps(mood), Bucket=s3_bucket, Key="{}/{}".format(server_details_key,s3_filename))                 
   return "Stored the Mood Items in {}".format(s3_filename)

def lambda_handler(event, context):
    
    logger.info("Received a event: {}".format(event))       
    mood = event
    result = store_mood_item(mood)
    
    return {
        'statusCode': 200,
        'body': 'OK',
        'headers': {
            'Content-Type': 'text/plain'
        }
    }    