import json
import requests
import boto3
import openpyxl
import urllib
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    print("Bucket: "+bucket)
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print("Key: "+key)
    s3_data = s3.get_object(Bucket=bucket,Key=key)
    file = s3_data['Body'].read()
    wb = openpyxl.load_workbook(io.BytesIO(file), data_only=True)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
