import json
import boto3
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        
        bucket_names = [bucket['Name'] for bucket in response['Buckets']]
        result = {
            "statusCode": 200,
            "body": json.dumps({
                "message": "List of S3 buckets",
                "buckets": bucket_names
            })
        }
        
        logger.info(f"Returning result: {event}")
        return result
    except Exception as e:
        logger.error(f"Error: {e}")
        result = {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Error fetching bucket list",
                "error": str(e)
            })
        }
        
        logger.info(f"Returning error result: {result}")
        return result
