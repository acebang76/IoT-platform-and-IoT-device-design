import json
import boto3
from decimal import Decimal
import urllib.request
import urllib.parse
import urllib.error

print('Loading funciton')

rekognition = boto3.client('rekognition')

def detect_labels(bucket, key):
    response = rekognition.detect_labels(Image={"S3Object": {"Bucket": bucket, "Name": key}})
    return response

def lambda_handler(event, context):
    # TODO implement
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    try:
        response = detect_labels(bucket, key)

        print(response)
        
        return response
    except Exception as e:
        print(e)

