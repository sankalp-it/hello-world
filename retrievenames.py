def lambda_handler(event, context):
    try:
        # Detect if body is present (API Gateway), otherwise treat event as direct
        if 'body' in event:
            body = event['body']
            if isinstance(body, str):
                body = json.loads(body)
        else:
            body = event  # invoked manually or from another Lambda

        # Now validate inputs
        rule_year = body.get('rule_year')
        model = body.get('model')

        if not rule_year or not model:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required parameters: rule_year or model'})
            }

        # Your repository call
        result = repo.get_vehicle_entry(rule_year, model)

        if not result:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': f'No standards found for {model} ({rule_year})'})
            }

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
