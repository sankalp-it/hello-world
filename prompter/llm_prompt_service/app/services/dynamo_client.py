import boto3
import os
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name=os.getenv("AWS_REGION", "us-east-1"))
table_name = os.getenv("DYNAMODB_TABLE", "LLMPrompts")
table = dynamodb.Table(table_name)

def save_prompt(prompt_id: str, prompt_text: str):
    table.put_item(Item={"prompt_id": prompt_id, "prompt_text": prompt_text})

def get_prompt(prompt_id: str):
    try:
        response = table.get_item(Key={"prompt_id": prompt_id})
        return response.get("Item")
    except ClientError as e:
        raise Exception(f"DynamoDB error: {e.response['Error']['Message']}")
