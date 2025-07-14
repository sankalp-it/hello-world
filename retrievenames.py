import json
from my_repository import MYEmissionWarrantyRuleRepository

# Initialize the repository with the table name
repo = MYEmissionWarrantyRuleRepository('VehicleStandards')

def lambda_handler(event, context):
    try:
        # Support API Gateway or direct invocation
        body = event.get('body')
        if isinstance(body, str):
            body = json.loads(body)

        # Extract inputs from request
        rule_year = body.get('rule_year')
        model = body.get('model')

        # Validate required fields
        if not rule_year or not model:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required parameters: rule_year or model'})
            }

        # Query DynamoDB via repository
        result = repo.get_vehicle_entry(rule_year, model)

        if not result:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': f'No standards found for {model} ({rule_year})'})
            }

        # Return the result as JSON
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(result)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
