import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url='http://localhost:8001')

table_name = "LLMPrompts"

existing_tables = [table.name for table in dynamodb.tables.all()]
if table_name not in existing_tables:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": "prompt_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "prompt_id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}
    )
    print(f"Table {table_name} is being created...")
else:
    print(f"Table {table_name} already exists.")
