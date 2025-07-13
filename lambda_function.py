import boto3
from parser import VehicleStandardsParser
from my_repository import MYEmissionWarrantyRuleRepository
import json

s3 = boto3.client('s3')
repo = MYEmissionWarrantyRuleRepository('VehicleStandards')


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    parser = VehicleStandardsParser(content)
    for record in parser.parse():
        item = {
            'PK': f"VEHICLE#{record.year}#{record.model.upper()}",
            'year': int(record.year),
            'make': record.make,
            'model': record.model,
            'vehicle_rules': record.model_rules,
            'model_year_rules': record.model_year_rules,
            'standards': record.standards_map
        }
        repo.insert_vehicle_entry(item)

    return {
        'statusCode': 200,
        'body': json.dumps('Upload complete and data inserted.')
    }
