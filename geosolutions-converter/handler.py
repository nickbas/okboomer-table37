import json
import geopandas as gpd
import os
import boto3
import urllib
from io import BytesIO
try:
  import unzip_requirements
except ImportError:
  pass

print('loading fsunction')

s3 = boto3.resource('s3')

def hello(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'])
    target_bucket = 'awstesttarget'
    awsRegion = event['Records'][0]['awsRegion']
    copy_source = {'Bucket':source_bucket, 'Key':key}
    # body = {
    #     "message": "Go Serverless v1.0! Your funsdfsasdasdfdction execuyuuuyuyuted successfully!!!!",
    #     "input": event
    # }
    try:
        print('Waiting for the file persist in the source bucket')
        # obj = s3.Object(source_bucket, key)
        # body = obj.get()['Body'].read()
        url = 'https://' + source_bucket + '.s3.' + awsRegion + '.amazonaws.com' + '/' + key
        df_fp = gpd.read_file(url)
        fp_test = df_fp
        csv_buffer = BytesIO()
        fp_test.to_csv(csv_buffer)
        s3_resource.Object(target_bucket, 'df.csv').put(Body=csv_buffer.getValue())
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the blah blah blah')
        raise e

    return response

    # Use this cdsdsdode if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
