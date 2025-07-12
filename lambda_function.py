import boto3
from parser import VehicleStandardsParser
import json

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
table = dynamodb.Table('VehicleStandards')


def lambda_handler(event, context):
    # Get bucket and key from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Read file from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    # Process using parser class
    parser = VehicleStandardsParser(content)
    for record in parser.parse():
        item = {
            'PK': f"VEHICLE#{record.year}#{record.model.upper()}",
            'SK': 'STANDARD',
            'year': int(record.year),
            'make': record.make,
            'model': record.model,
            'vehicle_rules': record.model_rules,
            'model_year_rules': record.model_year_rules,
            'standards': record.standards_map
        }

        table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps('Upload complete and data inserted.')
    }
